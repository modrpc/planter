import asyncio

import modpy
from .callargs import normalize

def proc_start():
    return

def proc_kill():
    return

def run_cmd_start(cmd, selfnode, *vars):
    args = vargs[0]
    if (len(args) < 1):
        print(cmd.usage)
        return

    try:
        uri = args[0]
        callargs = list(map(normalize, args[1:]))
        result = start(selfnode.event_loop(), uri, *callargs)
    except Exception as e:
        print("ERROR:", e)

def run_cmd_kill(cmd, selfnode, *vars):
    args = vargs[0]
    if (len(args) < 1):
        print(cmd.usage)
        return

    try:
        uri = args[0]
        callargs = list(map(normalize, args[1:]))
        result = start(selfnode.event_loop(), uri, *callargs)
    except Exception as e:
        print("ERROR:", e)
        
