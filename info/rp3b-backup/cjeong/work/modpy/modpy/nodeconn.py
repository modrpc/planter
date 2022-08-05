""" Node connections. """

class NodeConn:

    def __init__(self, tag):
        self._tag = tag
        self._conns = {}

    def add_conn(self, nodename):
        if nodename not in self._conns:
            self._conns.add(nodename)

    def conns(self):
        return self_conns
    

class NodeConnIterator:
    def __init__(self, tag):

    def __iter__(self):
        return self

    def __next__(self):
        

nodeconns = {}

def add_conn(tag, nodename):
    nodeconn = None
    if tag not in nodeconns.keys():
        nodeconn = NodeConn(tag)
        nodeconns[tag] = nodeconn
    else:
        nodeconn = nodeconns[nodename]

    nodeconn.add_conn(nodename)
            

def remove_conn(tag, nodename):
    if tag not in nodeconns.keys():
        return
    nodeconn = nodeconns[nodename]
    nodecon.remove_conn(nodename)


def conn_generator(tag):
    if (Tag not in nodeconns.keys():
        yield None
    nodeconn = nodeconns[nodename]
    for conn in nodeconn.conns():
        yield 
    
