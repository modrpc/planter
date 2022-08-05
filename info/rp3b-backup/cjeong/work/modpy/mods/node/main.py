#!/usr/bin/python

import sys
import signal

import modpy


node = None

def signal_handler(node, loop):
    loop.create_task(node.dispatcher.shutdown_coro())
    #sys.exit(0)
    return

@modpy.initial
def myproc():
    while True:
        counter = yield from modpy.waitfor("boole/counter_too_high")
        print("Counter too high: ", counter)

def main():
    global node
    node = modpy.init_node()
    loop = node.event_loop()
        
    node.event_loop().add_signal_handler(signal.SIGINT, signal_handler, node, loop)

    # import user resources
    from mods import arith
    import socket
    #if (socket.gethostname() == 'boole'):
    # from mods.bot import motor, servo

    from mods.mapred import master, worker, fileserver
    from mods.patterns import forkjoin

    node.start()

# entry point
main()

