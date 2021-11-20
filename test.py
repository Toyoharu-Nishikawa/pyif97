import numpy as np
from pyif97 import if97
a=if97.pt2h(1,500)
b=if97.ps2t(20.1, 6.9)
p = np.array([1,2,3])
t = np.array([500,510,520])
c = if97.pt2h(p,t)
mu=if97.ph2mu(1,3000,0)
ver = if97.version()
print(a)
print(b)
print(c)
print(ver)
print(mu)
