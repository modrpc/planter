import asyncio

import modpy

from .callargs import normalize


def subscribe(loop, uri):
    print("TODO")

def callback(fut):
    sys.stdout.write('Callback Result: %r\n' % fut.result())
    sys.stdout.write('MODPY> ')
    sys.stdout.flush()

def run_cmd_subscribe(cmd, loop, *vargs):
    args = vargs[0]
    if (len(args) < 1):
        print(cmd.usage)
        return

    try:
        uri = args[0]
        subscribe()
    except Exception as e:
        print("ERROR:", e)

    return 1

