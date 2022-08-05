import sys
import threading

from .command import Command

class Shell:
    def __init__(self, node, debug):
        self._node = node
        self._debug = debug

    def node(self):
        return self._node

    def debug(self):
        return self._debug

    def print_prompt(self):
        sys.stdout.write('MODPY> ')
        sys.stdout.flush()

    def run(self):
        import time
        time.sleep(1)

        Command.init(self._node)
        self.print_prompt()
        while True:
            line = input()
            words = line.split()
            if len(words) > 0:
                Command.process(line)
            self.print_prompt()
    
class ShellThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        if self.is_alive() == True:
            self.stop_event.set()
            self.join()
                
