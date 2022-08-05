""" ModRPC client responsible for sending messages. """

import asyncio
import socket

from . import message
from .util import logger
from .util import addr_to_netaddr

class Call:
    """
    Represents a single call instance.
    """

    def __init__(self, message, loop):
        self.message = message
        self.queue = asyncio.Queue(loop=loop)
        
    def __repr__(self):
        return "<%s:%s(%r)>" % (self.header.destaddr,
                                self.body.resource,
                                self.body.args)


class CallClient:
    """
    Responsible for taking a message from the output queue and then 
    sending requests to destinations.
    """
    callmap = {}
    callseq = 0
   
    def __init__(self, codec, tcp_port, mcast_addr, mcast_port, selfaddr,
                 input_queue, output_queue, loop):
        # input_queue is needed for quick return due to connection
        # error or server error
        self.codec = codec
        self.tcp_port = tcp_port
        self.mcast_addr = mcast_addr
        self.mcast_port = mcast_port
        self.addr = selfaddr
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.loop = loop

        self.reuseport = False
        try:
            sock.So_REUSEPORT
            self.reuseport = True
        except Exception:
            pass
        
        self.mcast_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.mcast_sockaddr = (self.mcast_addr, self.mcast_port)
        #self.mcast_sock.bind(self.mcast_sockaddr)

    @asyncio.coroutine
    def send_coro(self):
        """
        A coroutine which waits for outgoing messages and send them.
        """
        while True:
            m = yield from self.output_queue.get()
            logger.debug("[SEND] Request: %s" % m)
            if (m == message.IMESG_SHUTDOWN):
                print("Closing RPC client...")
                return
            destaddr = m.header.destaddr
            encm = self.codec.encode_message(m)

            if (m.body.tag < message.MESG_BCAST):
                # RPC calls
                try:
                    if (destaddr == self.addr):
                        # local call
                        print("...LOCAL CALL", m.body)
                        yield from self.input_queue.put(m)
                        continue
                    
                    print("...TCP CALL", m.body)
                    netaddr = addr_to_netaddr(destaddr)
                    ip = netaddr.ipaddr
                    port = netaddr.port
                    reader, writer = yield from \
                        asyncio.open_connection(ip, port, loop=self.loop)
                except Exception as e:
                    print("Connection failed: dest=%s" % (destaddr), str(e))
                    r = message.create(message.MESG_RETURN,
                                       m.header.destaddr,
                                       m.header.srcaddr,
                                       message.RESULT_ERROR,
                                       message.ERROR_CONNFAIL)
                    r.header.callid = m.header.callid
                    yield from self.input_queue.put(r)
                    if (not writer.is_closing()):
                        writer.close()
                    continue

                try: 
                    writer.write(encm.encode())
                    reply = yield from reader.read(100)
                    writer.close()

                except Exception as e:
                    print("No ACK: dest=%s" % (destaddr), str(e))
                    r = message.create(message.MESG_RETURN,
                                       m.header.destaddr,
                                       m.header.srcaddr,
                                       message.RESULT_ERROR,
                                       message.ERROR_NOACK)
                    r.header.callid = m.header.callid
                    yield from self.input_queue.put(r)
                    if (not writer.is_closing()):
                        writer.close()
                    continue
                
            else: 
                # Broadcast (m.body.tag == message.MESG_BCAST)
                try:
                    #print("...UDP CALL", m.body.tag)
                    self.loop.create_task(self.broadcast(encm))
                    
                except Exception as e:
                    print("Broadcast failure", e)
                    continue

    @asyncio.coroutine
    def broadcast(self, encm):
        self.mcast_sock.sendto(encm.encode(), self.mcast_sockaddr)
