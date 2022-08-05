import asyncio

import modpy
from .callargs import normalize


#cmd_call = None

def call(loop, noret, uri, *args):
    try:
        if (noret == 0):
            call_coro = modpy.call(uri, *args)
            future = asyncio.run_coroutine_threadsafe(call_coro, loop)

            #XXX: timeout is set to 10; for discovery, it may take time;
            #XXX: what is the right value?
            result = future.result(10)
            return result
        else:
            call_coro = modpy.callnr(uri, *args)
            asyncio.run_coroutine_threadsafe(call_coro, loop)
            return 
            
    except Exception as e:
        raise e

def run_cmd_callnr(cmd, selfnode, *vargs):
    args = vargs[0]
    if (len(args) < 1):
        print(cmd.usage)
        return

    try:
        uri = args[0]
        callargs = list(map(normalize, args[1:])) 
        result = call(selfnode.event_loop(), 1, uri, *callargs)
        print("RESULT:", result)

    except Exception as e:
        print("ERROR:", e)

    return 1

def run_cmd_call(cmd, selfnode, *vargs):
    args = vargs[0]
    if (len(args) < 1):
        print(cmd.usage)
        return

    try:
        uri = args[0]
        callargs = list(map(normalize, args[1:]))
        result = call(selfnode.event_loop(), 0, uri, *callargs)
        print("RESULT:", result)

    except Exception as e:
        print("ERROR:", e)

    return 1

