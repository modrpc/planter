import modpy


_fileidx = 0
_openfiles = {}

class File:
    def __init__(self, filename):
        global _fileidx
        global _openfiles
        try:
            self.fileobj = open(filename, "r")
            self.handle = _fileidx
            _openfiles[_fileidx] = self.fileobj
            _fileidx = _fileidx + 1

        except Exception as e:
            raise e

def _get_file(handle):
    if (handle in _openfiles.keys()):
        return _openfiles[handle]
    else:
        raise Exception("Invalid file name: %d" % handle)
        
    
@modpy.func
def file_open(filename):
    try:
        f = File(filename)
        return f.handle
    
    except Exception as e:
        raise e

@modpy.func
def file_readline(handle):
    try:
        f = _get_file(handle)
        line = f.readline(1024)
        if (not line):
            return "_EOF_"
        return line
    except Exception as e:
        raise e

@modpy.func
def file_close(handle):
    try:
        f = _get_file(handle)
        f.close()
    except Exception as e:
        raise e
