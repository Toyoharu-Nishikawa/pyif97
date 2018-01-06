from pyif97 import if97
a=if97.pt2h(1,500)
mu=if97.pt2mu(10,300)
ver = if97.version()
print(a)
print(ver.decode('utf-8'))
print(mu)
