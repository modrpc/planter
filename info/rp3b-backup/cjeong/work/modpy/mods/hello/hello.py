# hello.py
import modpy

@modpy.func
def sayhello(name):
 return "Hello, " + name

node = modpy.init_node().start()
