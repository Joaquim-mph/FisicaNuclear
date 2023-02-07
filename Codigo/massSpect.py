u = 1.661e-24 # g
mC12 = 12*u # g
mC14 = 14*u # g
B = 1e4 # G
e = 4.8e-10 # statC
r = 100 # cm
c = 29979245800 # cm/s
 
def eSpect(m,q,B,r):
    '''
    Use cm, g, s
    '''
    return ((q*B*r)**2)/(2*m*c**2)

def rSpect(m,q,B,E):
    '''
    Use cm, g, s
    Energia en ergs
    '''
    return (c/q/B)*(2*m*E)**0.5

def erg2eV(Energy):
    return Energy*6.24151e11

def erg2MeV(Energy):
    return Energy*624151
624151

E0 = eSpect(mC12,e,B,r)
E1 = erg2MeV(eSpect(mC12,e,B,r))
E2 = erg2MeV(eSpect(mC12,2*e,B,r))
E3 = erg2MeV(eSpect(mC12,3*e,B,r))
E4 = erg2MeV(eSpect(mC12,4*e,B,r))
E5 = erg2MeV(eSpect(mC12,5*e,B,r))

l = [E1,E2,E3,E4,E5]

#for e in l:
#    print(round(e,2))

E6 = erg2MeV(eSpect(mC12,e,B,50))
E7 = erg2MeV(eSpect(mC12,e,B,25))

r1 = rSpect(mC12,e,B,E0)
r2 = rSpect(mC12,2*e,B,E0)
r3 = rSpect(mC12,3*e,B,E0)

r = [r1,r2,r3]

r4 = rSpect(mC14,e,B,E0)
r5 = rSpect(mC14,2*e,B,E0)
r6 = rSpect(mC14,3*e,B,E0)

dm = (e*B*0.05)**2/(2*E0)