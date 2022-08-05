import argparse
import signal
import logging
import threading

import modpy

from . import dirconfig
from .shell import Shell

def signal_handler(signal, frame):
    sys.exit(0)

def start_node(node):
    node.start()

def init_shell(node):
    debug = False;

    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true",
                        dest="debug", default=debug,
                        help="Print asyncio debug messages.")

    shell = Shell(node, debug)
    return shell


def main():
    # init
    dirconfig.init()
    signal.signal(signal.SIGINT, signal_handler)

    node = modpy.init_node()
    shell = init_shell(node)
    loop = node.event_loop()

    print("node:", node)
    
    if (shell.debug()):
        logging.basicConfig(level=logging.DEBUG)
        loop.set_debug(True)

    try:
        modpy_thr = threading.Thread(target=start_node, args=(node, ))
        modpy_thr.start()
        
        #shell_thr = threading.Thread(target=shell, args=(node, ))
        #shell_thr.start()
        shell.run()
    except (KeyboardInterrupt, SystemExit):
        modpy.stop_node()
        sys.exit(0)
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
