from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from hermite_QM import *
import nuclear as nu

V0= 50e6 # ev
a=0.5 # fm
n = 100
A = 20
Z = 10
hBar = 1 #6.582119569e-16 # ev*s
m = nu.massIsotope(nu.buscaZA(Z,A)[0])
R = nu.radio(A)
psi0 = 0
dotpsi0 = 0.1
V0= a*np.log(1+np.exp(R/a))# ev

# Space Lattice
radii = np.linspace(0,R*1.5,n)
dr = radii[1]-radii[0]
cte = (m*dr**2)/(hBar**2)

plt.clf
potential = lambda r: -V0/(1+np.exp((r-R)/a))
vals, vecs = eigenstates(potential, nterms=11, ngpts=12)
print(np.round(vals[:7], 6))
fig, ax = plt.subplots(1, 1)
plot_eigenstates(vals, vecs, potential,lims=(0.1,7))
plt.show()

# Potencial
def potentialWS(r):
    return -V0/(1+np.exp((r-R)/a))
V = potentialWS(radii)


