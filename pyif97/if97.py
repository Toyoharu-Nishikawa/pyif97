import os
import numpy as np
from ctypes import *
import warnings

rootPath=os.path.dirname(os.path.abspath( __file__ ))

if os.name =='posix':
    _lib =  cdll.LoadLibrary(os.path.join(rootPath,"SteamTable_IF97.so"))
elif os.name == 'nt':
    _lib =  windll.LoadLibrary(os.path.join(rootPath,"SteamTable_IF97.dll"))
else:
    print("unsupported OS")

def _safe_set_types(lib, funcname, restype, argtypes):
    try:
       getattr(_lib, funcname).restype = restype
       getattr(_lib, funcname).argtypes = argtypes
    except AttributeError:
       warnings.warn("&s is not defined. % funcname", ImportWarning, stacklevel=1)


#arguments type and result type
#version
_safe_set_types(_lib, "IF97_version",restype=c_char_p, argtypes=None)

#pt
_safe_set_types(_lib, "IF97_pt2g", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_pt2u", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_pt2v", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_pt2h", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_pt2s", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_pt2w", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_pt2w", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_pt2MM", restype=c_int, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_pt2cp", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_pt2cv", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_pt2k", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_pt2mu", restype=c_double, argtypes=[c_double,c_double])


#ph
_safe_set_types(_lib, "IF97_ph2g", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ph2u", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ph2v", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ph2t", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ph2s", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ph2w", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ph2x", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ph2MM", restype=c_int, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ph2mu", restype=c_double, argtypes=[c_double,c_double,c_int])
_safe_set_types(_lib, "IF97_ph2cp", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ph2cv", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ph2k", restype=c_double, argtypes=[c_double,c_double])


#ps
_safe_set_types(_lib, "IF97_ps2g", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ps2u", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ps2v", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ps2t", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ps2h", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ps2w", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ps2x", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ps2k", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_ps2MM", restype=c_int, argtypes=[c_double,c_double])


#hs
_safe_set_types(_lib, "IF97_hs2g", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_hs2u", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_hs2p", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_hs2t", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_hs2v", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_hs2w", restype=c_double, argtypes=[c_double,c_double])
_safe_set_types(_lib, "IF97_hs2x", restype=c_double, argtypes=[c_double,c_double])


#SAT
_safe_set_types(_lib, "IF97_SATp2t", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATt2p", restype=c_double, argtypes=[c_double])


#SATlp
_safe_set_types(_lib, "IF97_SATlp2g", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlp2u", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlp2t", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlp2v", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlp2h", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlp2s", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlp2w", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlp2cp", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlp2cv", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlp2k", restype=c_double, argtypes=[c_double])


#SATgp
_safe_set_types(_lib, "IF97_SATgp2g", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgp2u", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgp2t", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgp2v", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgp2h", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgp2s", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgp2w", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgp2cp", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgp2cv", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgp2k", restype=c_double, argtypes=[c_double])


#SATlt
_safe_set_types(_lib, "IF97_SATlt2g", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlt2u", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlt2p", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlt2v", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlt2h", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlt2s", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlt2w", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlt2cp", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlt2cv", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATlt2k", restype=c_double, argtypes=[c_double])



#SATgt
_safe_set_types(_lib, "IF97_SATgt2g", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgt2u", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgt2p", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgt2v", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgt2h", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgt2s", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgt2w", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgt2cp", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgt2cv", restype=c_double, argtypes=[c_double])
_safe_set_types(_lib, "IF97_SATgt2k", restype=c_double, argtypes=[c_double])


#def
#version
def version():
  return _lib.IF97_version().decode('utf8')
#pt
def pt2g(p,t):
    return np.vectorize(_lib.IF97_pt2g)(p,t)

def pt2u(p,t):
    return np.vectorize(_lib.IF97_pt2u)(p,t)

def pt2v(p,t):
    return np.vectorize(_lib.IF97_pt2v)(p,t)

def pt2h(p,t):
    return np.vectorize(_lib.IF97_pt2h)(p,t)

def pt2s(p,t):
    return np.vectorize(_lib.IF97_pt2s)(p,t)

def pt2w(p,t):
    return np.vectorize(_lib.IF97_pt2w)(p,t)

def pt2MM(p,t):
    return np.vectorize(_lib.IF97_pt2MM)(p,t)

def pt2cp(p,t):
    return np.vectorize(_lib.IF97_pt2cp)(p,t)

def pt2cv(p,t):
    return np.vectorize(_lib.IF97_pt2cv)(p,t)

def pt2k(p,t):
    return np.vectorize(_lib.IF97_pt2k)(p,t)

def pt2mu(p,t):
    return np.vectorize(_lib.IF97_pt2mu)(p,t)

#ph
def ph2g(p,h):
    return np.vectorize(_lib.IF97_ph2g)(p,h)

def ph2u(p,h):
    return np.vectorize(_lib.IF97_ph2u)(p,h)

def ph2v(p,h):
    return np.vectorize(_lib.IF97_ph2v)(p,h)

def ph2t(p,h):
    return np.vectorize(_lib.IF97_ph2t)(p,h)

def ph2s(p,h):
    return np.vectorize(_lib.IF97_ph2s)(p,h)

def ph2w(p,h):
    return np.vectorize(_lib.IF97_ph2w)(p,h)

def ph2x(p,h):
    return np.vectorize(_lib.IF97_ph2x)(p,h)

def ph2MM(p,h):
    return np.vectorize(_lib.IF97_ph2MM)(p,h)

def ph2mu(p,h,n):
    return np.vectorize(_lib.IF97_ph2mu)(p,h,n)

def ph2cp(p,h):
    return np.vectorize(_lib.IF97_ph2cp)(p,h)

def ph2cv(p,h):
    return np.vectorize(_lib.IF97_ph2cv)(p,h)

def ph2k(p,h):
    return np.vectorize(_lib.IF97_ph2k)(p,h)

#ps
def ps2g(p,s):
    return np.vectorize(_lib.IF97_ps2g)(p,s)

def ps2u(p,s):
    return np.vectorize(_lib.IF97_ps2u)(p,s)

def ps2v(p,s):
    return np.vectorize(_lib.IF97_ps2v)(p,s)

def ps2t(p,s):
    return np.vectorize(_lib.IF97_ps2t)(p,s)

def ps2h(p,s):
    return np.vectorize(_lib.IF97_ps2h)(p,s)

def ps2w(p,s):
    return np.vectorize(_lib.IF97_ps2w)(p,s)

def ps2x(p,s):
    return np.vectorize(_lib.IF97_ps2x)(p,s)

def ps2k(p,s):
    return np.vectorize(_lib.IF97_ps2k)(p,s)

def ps2MM(p,s):
    return np.vectorize(_lib.IF97_ps2MM)(p,s)

#hs
def hs2g(h,s):
    return np.vectorize(_lib.IF97_hs2g)(h,s)

def hs2u(h,s):
    return np.vectorize(_lib.IF97_hs2u)(h,s)

def hs2p(h,s):
    return np.vectorize(_lib.IF97_hs2p)(h,s)

def hs2t(h,s):
    return np.vectorize(_lib.IF97_hs2t)(h,s)

def hs2v(h,s):
    return np.vectorize(_lib.IF97_hs2v)(h,s)

def hs2w(h,s):
    return np.vectorize(_lib.IF97_hs2w)(h,s)

def hs2x(h,s):
    return np.vectorize(_lib.IF97_hs2x)(h,s)

#SAT
def SATp2t(p):
    return np.vectorize(_lib.IF97_SATp2t)(p)

def SATt2p(t):
    return np.vectorize(_lib.IF97_SATt2p)(t)

#SATlp
def SATlp2g(p):
    return np.vectorize(_lib.IF97_SATlp2g)(p)

def SATlp2u(p):
    return np.vectorize(_lib.IF97_SATlp2u)(p)

def SATlp2t(p):
    return np.vectorize(_lib.IF97_SATlp2t)(p)

def SATlp2v(p):
    return np.vectorize(_lib.IF97_SATlp2v)(p)

def SATlp2h(p):
    return np.vectorize(_lib.IF97_SATlp2h)(p)

def SATlp2s(p):
    return np.vectorize(_lib.IF97_SATlp2s)(p)

def SATlp2w(p):
    return np.vectorize(_lib.IF97_SATlp2w)(p)

def SATlp2cp(p):
    return np.vectorize(_lib.IF97_SATlp2cp)(p)

def SATlp2cv(p):
    return np.vectorize(_lib.IF97_SATlp2cv)(p)

def SATlp2k(p):
    return np.vectorize(_lib.IF97_SATlp2k)(p)

#SATgp
def SATgp2g(p):
    return np.vectorize(_lib.IF97_SATgp2g)(p)

def SATgp2u(p):
    return np.vectorize(_lib.IF97_SATgp2u)(p)

def SATgp2t(p):
    return np.vectorize(_lib.IF97_SATgp2t)(p)

def SATgp2v(p):
    return np.vectorize(_lib.IF97_SATgp2v)(p)

def SATgp2h(p):
    return np.vectorize(_lib.IF97_SATgp2h)(p)

def SATgp2s(p):
    return np.vectorize(_lib.IF97_SATgp2s)(p)

def SATgp2w(p):
    return np.vectorize(_lib.IF97_SATgp2w)(p)

#SATlt
def SATlt2g(t):
    return np.vectorize(_lib.IF97_SATlt2g)(t)

def SATlt2u(t):
    return np.vectorize(_lib.IF97_SATlt2u)(t)

def SATlt2p(t):
    return np.vectorize(_lib.IF97_SATlt2p)(t)

def SATlt2v(t):
    return np.vectorize(_lib.IF97_SATlt2v)(t)

def SATlt2v(t):
    return np.vectorize(_lib.IF97_SATlt2v)(t)

def SATlt2h(t):
    return np.vectorize(_lib.IF97_SATlt2h)(t)

def SATlt2s(t):
    return np.vectorize(_lib.IF97_SATlt2s)(t)

def SATlt2w(t):
    return np.vectorize(_lib.IF97_SATlt2w)(t)

def SATlt2cp(t):
    return np.vectorize(_lib.IF97_SATlt2cp)(t)

def SATlt2cv(t):
    return np.vectorize(_lib.IF97_SATlt2cv)(t)

def SATlt2k(t):
    return np.vectorize(_lib.IF97_SATlt2k)(t)

#SATgt
def SATgt2g(t):
    return np.vectorize(_lib.IF97_SATgt2g)(t)

def SATgt2u(t):
    return np.vectorize(_lib.IF97_SATgt2u)(t)

def SATgt2p(t):
    return np.vectorize(_lib.IF97_SATgt2p)(t)

def SATgt2v(t):
    return np.vectorize(_lib.IF97_SATgt2v)(t)

def SATgt2h(t):
    return np.vectorize(_lib.IF97_SATgt2h)(t)

def SATgt2s(t):
    return np.vectorize(_lib.IF97_SATgt2s)(t)

def SATgt2w(t):
    return np.vectorize(_lib.IF97_SATgt2w)(t)

def SATgt2cp(t):
    return np.vectorize(_lib.IF97_SATgt2cp)(t)

def SATgt2cv(t):
    return np.vectorize(_lib.IF97_SATgt2cv)(t)

def SATgt2k(t):
    return np.vectorize(_lib.IF97_SATgt2k)(t)
