import modpy
import hashlib


def get_hexdigest(str):
    m = hashlib.sha256()
    m.update(byte(str))
    return m.hexdigest()

def gen_nouce():
    

@modpy.func
def get_nounce():
    return 123

