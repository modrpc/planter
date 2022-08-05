# hello.py
import modpy

# ModPy initial functions are executed once when the node starts
@modpy.initial
def onboard():
   yield from modpy.broadcast("sayhello", modpy.self_nodename())

@modpy.func
def sayhello(nodename):
 return "Hello from " + nodename

node = modpy.init_node().start()
