import asyncio
import modpy

counter = 1;

@modpy.func
def set_counter(v):
    global counter
    counter = v

@modpy.func
def get_counter():
    global counter
    return counter

@modpy.func
def add(a, b):
    return a + b

@modpy.func
def inc(v):
    return v + 1


@modpy.func
def add2(a, b):
    global counter
    counter = counter + a + b
    if (counter > 5):
        print("FIRE counter_too_high")
        yield from modpy.fire("counter_too_high", counter)
    return a + b + 100

@modpy.event
def counter_too_high():
    return counter

@modpy.event
def target_counter_reached():
    return counter

@modpy.func
def sub(a, b):
    # gauss.add(a, b)
    result = yield from modpy.call('plato', 'add', a, b)
    return result - 10

@modpy.event
def counter_changed():
    return counter

@modpy.proc
def watch_counter_proc(target_val):
    while True:
        yield from asyncio.sleep(1)
        if (counter == target_val):
            yield from modpy.fire("target_counter_reached", counter)
            saved_counter = counter
            
@modpy.func
def watch_counter():
    saved_counter = counter
    while True:
        yield from asyncio.sleep(1)
        if (counter != saved_counter):
            yield from modpy.fire("counter_changed", counter)
            saved_counter = counter

@modpy.func
def wait_for_counter_too_high():
    while True:
        val = yield from modpy.waitfor("gauss", "counter_too_high")
        print("COUNTER: ", val)


@modpy.func
def pingpong(node):
    i = 0
    j = 0
    while True:
        val = yield from modpy.call("%s/add" % node, i, j)
        if ((i + j) != val):
            print("ERROR!:", i, j, val)
            import sys
            sys.exit(0)
        else:
            print(val)
        yield from asyncio.sleep(0.1)
        i = i + 1
        j = j + 1
