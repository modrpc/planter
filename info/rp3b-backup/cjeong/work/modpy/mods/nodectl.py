""" For management of worker nodes. """

import asyncio
import modpy


@modpy.func
def node_new(p):
    init_nodectl()
    

_parent = ""

@modpy.func
def set_parent(p):
    try:
        global _parent
        yield from modpy.call(p, "add_child", modpy.self_nodename())
        _parent = p
    except Excpetion as e:
        raise e

def get_parent():
    return _parent


_childnodes = []

@modpy.func
def add_child(child):
    # XXX: avoid duplicates
    _childnodes.append(child)

@modpy.func
def remove_child(child):
    _childnodes.remove(child)


    
