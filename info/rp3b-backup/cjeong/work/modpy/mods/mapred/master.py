import modpy



workers = []

@modpy.event
def worker_available():
    return True

@modpy.func
def register_worker(node):
    for worker in workers:
        if (worker == node):
            return False
    workers.append(node)

@modpy.func
def checkout_worker():
    if (len(workers) == 0):
        worker = yield from modpy.waitfor("worker_available")
    else:
        worker = workers[0]
        workers.remove(worker)
    return worker
        
    
@modpy.func
def checkin_worker(worker):
    if (len(workers) == 0):
        yield from modpy.fire("worker_available", worker)
    else:
        workers.append(node)
    print("\n===================================================\n")
    
@modpy.func
def mapreduce(njobs):
    doneset = []
    for i in range(njobs):
        ev = modpy.create_event("done%d" % i)
        doneset.append(ev)
    
    for i in range(njobs):
        worker = yield from modpy.call("checkout_worker")
        yield from modpy.callnr("%s/do_work" % worker, "MAP", "count_lines",
                                "/tmp/common.go", i)
    
    yield from modpy.waitfor_events(*doneset)
    print("DONE!")
