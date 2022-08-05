""" Node management. """

import argparse
import sys
import os
import asyncio
import socket
import atexit
import threading
import logging
import time

from . import util
from . import dispatch

DEFAULT_RPCPORT = 49898
DEFAULT_MCASTIP = "224.0.0.251"
DEFAULT_MCASTPORT = 49898
DEFAULT_MODPYROOT = "/opt/modrpc/modpy"

NODESTAT_INIT = 0
NODESTAT_CONN = 1

class Node:
    """ Node that represents the self node. """
    def __init__(self, name, rpcip, rpcport, mcastip, mcastport, modpyroot,
                 debug, verbose, loop):
        self._name = name
        self._rpcip = rpcip
        self._rpcport = rpcport
        self._mcastip = mcastip
        self._mcastport = mcastport
        self._modpyroot = modpyroot
        self._debug = debug
        self._verbose = verbose
        self._loop = loop

        self._addr = self._rpcip + ":" + str(self._rpcport)
        self._status = NODESTAT_CONN

        self.dispatcher = dispatch.Dispatcher(self._name,
                                              self._rpcip,
                                              self._rpcport,
                                              self._mcastip,
                                              self._mcastport,
                                              self._loop)
        self.loop = self.dispatcher.loop

        if (self._debug):
            logging.basicConfig(level=logging.DEBUG)

    def name(self):
        return self._name

    def addr(self):
        return self._addr

    def rpcip(self):
        return self._rpcip

    def rpcport(self):
        return self._rpcport

    def mcastip(self):
        return self._mcastip

    def mcastport(self):
        return self._mcastport

    def verbose(self):
        return self._verbose

    def debug(self):
        return self._debug

    def status(self):
        return self._status;
    
    def event_loop(self):
        return self.loop

    def start(self):
        self.dispatcher.start()

    def stop(self):
        self.dispatcher.stop()

    def thr_start(self):
        thr = threading.Thread(target=start, args=())
        thr.start() 

_node = None
def init_node(**params):
    """ Initialize the node. """

    name = params.pop("name", None)
    rpcport = params.pop("rpcport", DEFAULT_RPCPORT)
    mcastip = params.pop("mcastip", DEFAULT_MCASTIP)
    mcastport = params.pop("mcastport", DEFAULT_MCASTPORT)
    loop = params.pop("loop", None)
    debug = params.pop("debug", None)
    verbose = params.pop("verbose", None)
    
    global _node
    if (_node != None):
        print("Node already initialized...")
        return _node

    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str, action="store",
                        dest="name", default=name,
                        help="Set the name of node.")
    parser.add_argument("--rpcport", type=int, action="store",
                        dest="rpcport",
                        default=rpcport,
                        help="Set RPC port.")
    parser.add_argument("--mcastip", type=str, action="store",
                        dest="mcastip",
                        default=DEFAULT_MCASTIP,
                        help="Set multicast IP address.")
    parser.add_argument("--mcastport", type=int, action="store",
                        dest="mcastport",
                        default=DEFAULT_MCASTPORT,
                        help="Set multicast port.")
    parser.add_argument("--modpyroot", action="store_true",
                        dest="modpyroot", default=None,
                        help="Set MODPYROOT directory.")
    parser.add_argument("--debug", action="store_true",
                        dest="debug", default=debug,
                        help="Print asyncio debug messages.")
    parser.add_argument("--verbose", action="store_true",
                        dest="verbose", default=debug,
                        help="Verbose mode.")
    results = parser.parse_args()


    if (results.name == None):
        hostname = socket.gethostname()
        name = "%s_%d" % (hostname, rpcport)
    else:
        name = results.name
    rpcip = util.get_outbound_ip()
    rpcport = results.rpcport
    mcastip = results.mcastip
    mcastport = results.mcastport
    debug = results.debug
    

    modpyroot = results.modpyroot
    if modpyroot == None:
        modpyroot = os.environ.get("MODPYROOT")
        if modpyroot == None:
            modrpcroot = os.environ.get("MODRPCROOT")
            if modrpcroot != None:
                modpyroot = modrpcroot + "/pi"
            else:
                modpyroot = DEFAULT_MODPY_ROOT
                

    if (loop == None):
        if sys.platform == "win32" or sys.platform == "cygwin":
            loop = asyncio.ProactorEventLoop()
        elif sys.platform == "linux2":
            loop = asyncio.SelectorEventLoop()
        else:
            loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)

    rpcip = util.get_outbound_ip()
    
    _node = Node(name, rpcip, results.rpcport, results.mcastip,
                 results.mcastport, modpyroot, results.debug,
                 results.verbose, loop)
    print("Node initialized (Name=%s, RPC=%s:%d, MCAST=%s:%d)..."
          % (_node.name(), _node.rpcip(), _node.rpcport(), _node.mcastip(),
             _node.mcastport()))
    return _node

def stop_node():
    global _node
    if (_node != None):
        _node.stop()
    _node = None

def self_node():
    if (_node == None):
        raise Exception("Node not initialized")
    return _node

def self_nodename():
    if (_node == None):
        raise Exception("Node not initialized")
    return _node._name

def self_nodeaddr():
    if (_node == None):
        raise Exception("Node not initialized")
    return _node._addr
                                
