import modpy


_master = ""
_filesvr = ""

@modpy.func
def start_worker(master, filesvr):
    global _filesvr
    global _master
    _master = master
    _filesvr = filesvr
    yield from modpy.call("%s/register_worker" % _master, modpy.self_nodename())
    print ("FILESVR: ", _filesvr)

@modpy.final
def close_worker():
    global _master
    if (_master != ""):
        yield from modpy.call("%s/unregister_worker" % _master, modpy.self_nodename())
        _master = ""

@modpy.func
def do_work(mapred, fn, doneev, filename, index):
    yield from asyncio.sleep(2)
    if (mapred == "MAP"):
        yield from modpy.call(fn, filename, index)
        yield from modpy.call("%s/checkin_worker" % _master, modpy.self_nodename())
    elif (mapred == "RED"):
        yield from modpy.call(fn, filename, index)
        yield from modpy.call("%s/checkin_worker" % _master, modpy.self_nodename())
    else:
        return


@modpy.func
def count_lines(filename, index):
    try:
        nlines = 0;
        workfile = "%s.%d" % (filename, index)
        handle = yield from modpy.call("%s/file_open" % _filesvr, workfile)
        while True:
            line = yield from modpy.call("%s/file_readline" % _filesvr, handle)
            if (line == "_EOF_"):
                break;
            #print(line)
            nlines = nlines + 1
        yield from modpy.call("%s/file_close" % _filesvr, handle)
        return nlines
    except Exception as e:
        raise e
    
