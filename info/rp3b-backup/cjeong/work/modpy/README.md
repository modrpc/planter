# ModPy
ModPy is a Python library, based on [asyncio](https://docs.python.org/3/library/asyncio.html), which facilitates programming of autonomous nodes in distributed environments. Creating a service function in a node a node is as simple as adding a Python decorator <code>@modpy.func</code>. As an example,  
```python
  @modpy.func
  def sayhello(name):
     return "hello, " + name
```

Also, calling  a remote function is simple. Given that a ModPy node, named "gauss", contains the <code>sayhello</code> function, another node can access it as shown below:
```python
   result = await modpy.call("gauss/sayhello", "world")
   # result will be "hello, world"
```

# Getting Started

## Installation
Use pip to install the ModPy library. 

```bash
  $ pip3 install modpy
```

ModPy depends on the [asyncio](https://docs.python.org/3/library/asyncio.html) library, which was introduced in Python 3.4. Use Python 3.5 or later to use ModPy.


## Installation Testing
To test if the library is installed properly, create a node program which serves a ModPy function, sayhello.
```python
  import modpy
  @modpy.func
  def add(a, b):
    return a + b
  modpy.init_node().start()
```

Use the following command to run the node.

```bash
  $ python3 test.py --name gauss --rpcport 12346
```

Next, run the ModPy shell and call the <code>add</code> function.

```bash
  $ python3 -m modpy.shell.main
  MODPY> call gauss/sayhello 3 4
  RESULT: 7
```


# Documentation
ModPy is a library which implements the [ModRPC protocol](https://github.com/modrpc/modpy/wiki/ModRPC-Protocol) which is a simple protocol for remote resource access.  ModPy is a binding of ModRPC to the Python language. Another project for Golang binding is in progress and I have a future plan to develop C or C++ bindings (haven't decided between the two yet). 

* [Basic Concepts](https://github.com/modrpc/modpy/wiki/Basic-Concepts)
* [ModPy API](https://github.com/modrpc/modpy/wiki/ModPy-API)
* [ModPy Benefits](https://github.com/modrpc/modpy/wiki/Benefits)
* Examples: [HelloWorld](https://github.com/modrpc/modpy/wiki/Example:-Hello-World), [MapReduce](https://github.com/modrpc/modpy/wiki/Example:-MapReduce), [Raft](https://github.com/modrpc/modpy/wiki/Example:-MapReduce)
 dunk
* [ModRPC protocol](https://github.com/modrpc/modpy/wiki/ModRPC-Protocol)
* [Extending ModPy]
