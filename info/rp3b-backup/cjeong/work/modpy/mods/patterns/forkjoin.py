import modpy
import asyncio


@modpy.func
def fork(node0, node1):
    yield from modpy.callnr("%s/somework" % node0)
    yield from modpy.callnr("%s/somework" % node1)
    print("FORK_DONE")
    yield from join(node0, node1)

@modpy.func
def join(node0, node1):
    print("JOIN_BEGIN")
    yield from modpy.waitfor("%s/donework" % node0, "%s/donework"%  node1)
    print("JOIN_DONE")

@modpy.event
def donework():
    return True

@modpy.func
def somework():
    print("SOMEWORK BEGIN")
    me = modpy.self_nodename()
    if (me == "gauss"):
        yield from asyncio.sleep(3)
    else:
        yield from asyncio.sleep(4)
    print("SOMEWORK 0")
    yield from modpy.fire("donework", True)
    print("SOMEWORK END")
