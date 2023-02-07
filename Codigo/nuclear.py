# Programa para el curso FI6012 - Fisica Nuclear
# 'AME2016.txt' entrega los datos para el calculo
# de la masa para distintos nucleos atomicos.
# 1u = 931.494 MeV/c^2
# M_atom = A*u + Excess

import numpy as np
import matplotlib.pyplot as plt

u = 931.494 # MeV/c^2
me = 0.510998928 # MeV/c^2  {Masa electron}

### Cargar datos AME2016 ###

archivo = 'AME2016.txt'

def cargar(archivo):
    Archivo = open(archivo, "r")
    symbol = []
    Z = []
    A = []
    excess = []  # MeV
    k = 0
    for linea in Archivo:
        k += 1
        if k > 5 and k < 3444:
            linea = linea.strip()
            lista = linea.split(" ")
            symbol.append(lista[0][1:])
            excess.append(lista[-1])
            k1 = 0
            for i in range(1,len(lista)):
                if lista[i] == '' or lista[i] == "'":
                    continue
                else:
                    k1 += 1
                    # print(k1)
                    if k1 == 1:
                        Z.append(lista[i])
                        continue
                    elif k1 == 2:
                        A.append(lista[i])
                        continue
                    else:
                        continue
    simbolos=[]
    #limpiaSimbolos#
    for simbolo in symbol:
        limpia = simbolo.replace("'","")
        simbolos.append(limpia)
    return simbolos, Z, A, excess

simbolos, z, a, excess = cargar(archivo)

def buscaIsotopo(simbol):
    for i in range(len(simbolos)):
        if simbol == str(simbolos[i]):
            return [simbol,z[i],a[i],excess[i]]

def buscaZ(Z):
    '''
    Z --> int
    recibe un numero de protones retorna todos los isotopos 
    con ese numero de protones en el nucleo.
    '''
    l = []
    for i in range(len(a)):
        if str(Z) == z[i]:
            l.append(simbolos[i])
    return l

def buscaA(A):
    l = []
    for i in range(len(a)):
        if str(A) == a[i]:
            l.append(simbolos[i])
    return l

def buscaZA(Z,A):
    for i in range(len(a)):
        if str(A) == a[i] and str(Z) == z[i]:
            return simbolos[i]

def radio(A):
    return 1.25*A**(1/3)

def massIsotope(simbol):
    isotopo = buscaIsotopo(simbol)
    masa = float(isotopo[2])* u + float(isotopo[3])
    return masa

def diffMass(lista1,lista2):
    '''
    lista1 (list) --> primer conjunto de isotopos
    lista2 (list) --> segundo conjunto de isotopos
    -----------------------------------------------
    suma las masas de cada grupo de isotopos por separado
    calcula la diferencia de masa entre ambos grupos.
    -----------------------------------------------
    si la diferencia de masa es negativa, entonces energía
    es liberada en el movimiento de las masas resultantes
    diffMass<0 --> reaccion exotermica
    diffMass>0 --> reaccion endotermica
    -----------------------------------------------
    notar que la medida de masa es Mev/c^2, por lo que
    la energia cinetica será diffMass*c^2
    '''
    masa1 = 0
    masa2 = 0
    for i in lista1:
        masa1+=massIsotope(i)
    for j in lista2:
        masa2+=massIsotope(j)
    return masa2-masa1 # masa final menos masa inicial

def alphaDecayResult(Z,A):
    result = buscaZA(Z-2,A-4)
    return result

def alphaEnergy(Z,A):
    # resultados negativos implican perdidad de masa
    # Es decir que se libera energia, un valor positivo
    # implicaria que este decaimiento alpha requiere energia
    # externa para suceder, e.g. O20 para decaer por particula
    # alfa requiere ~17.771 MeV externos, por lo que es no
    # es probable este tipo decaimiento
    isotope = buscaZA(Z,A)
    result = buscaZA(Z-2,A-4)
    return diffMass([isotope],[result,'He4'])

def betaPlusDecay(Z,A):
    assert not Z == 0 and not A == 0
    return buscaZA(Z-1,A)

def betaMinusDecay(Z,A):
    assert not A == 0 # un neutron no decae en un neutron
    return buscaZA(Z+1,A)

def betaEnergy(Z,A,ePlus = None, eMinus = None):
    if Z == 0 and A == 1: # un neutron
        e = diffMass([buscaZA(Z,A)[0]],[betaMinusDecay(Z,A)[0]]) - me
        return [None,e]
    elif Z == 1 and A == 1: # un proton
        e = diffMass([buscaZA(Z,A)[0]],[betaPlusDecay(Z,A)[0]]) - me
        return [e,None]
    elif Z == 1:
        if betaMinusDecay(Z,A) == None:
            return [None,None]
        elif not betaMinusDecay(Z,A) == None:
            betaMinus = betaMinusDecay(Z,A)
            eMinus = diffMass([buscaZA(Z,A)],[betaMinus]) - me
            return [None,eMinus]
    else:
        betaPlus = betaPlusDecay(Z,A)
        betaMinus = betaMinusDecay(Z,A)
        if betaPlus == None:
            ePlus = None
        elif betaMinus == None:
            eMinus = None
        else:
            ePlus = diffMass([buscaZA(Z,A)],[betaPlus]) - me
            eMinus = diffMass([buscaZA(Z,A)],[betaMinus]) - me
        return [ePlus,eMinus]

def betaDecay(Z,A):
    e = betaEnergy(Z,A)
    if Z == 0 and A == 1: # un neutron
        print('Decaimiento beta-')
        return e[1]
    elif Z == 1 and A == 1: # un proton
        print('Decaimiento beta+')
        return e[0]
    if e[0] < 0:
        print('Decaimiento beta+')
        return e[0]
    elif e[1] < 0:
        print('Decaimiento beta-')
        return e[1]

def betaChoice(verdad=True, j=0):
    for i in range(len(a)):
        j+=1
        Z = int(z[i])
        A = int(a[i])
        e = betaEnergy(Z,A)
        if e[1] == None or e[0] == None:
            continue
        elif np.sign(e[0]) == np.sign(e[1]) == -1:
            print(i)
            verdad = False
    print(j)
    return verdad

def massDefect(Z,A):
    mp=massIsotope('p')
    mn=massIsotope('n')
    mZA=Z*mp+(A-Z)*mn
    return (mZA-massIsotope(buscaZA(Z,A)[0]))

def tunelAlpha(Z,A):
    '''
    Retorna la distancia en fermis (fm) del tunel que atraviesa
    la particula alpha en la que decae el nucleo (Z,A)
    '''
    return abs((400/137)*(Z-2)/alphaEnergy(Z,A)) - 1.2*A**(1/3)

#########################################################
# Arbol de decaimientos:
#########################################################
vec = []

class Node:     
    def __init__(self, x):         
        self.data = x
        self.child = []
 
    def creaHijos(self):
        raiz = buscaIsotopo(self.data)
        Z = int(raiz[1])
        A = int(raiz[2])
        alpha = alphaEnergy(Z,A)
        beta = betaEnergy(Z,A)
        if alpha<0:
            self.child.append(Node(alphaDecayResult(Z,A)))
        if beta[0]<0:
            self.child.append(Node(betaPlusDecay(Z,A)))
        if beta[1]<0:
            self.child.append(Node(betaMinusDecay(Z,A)))
        return self
    
    def printPath(self,vec):
        for ele in vec:
            print(ele, end = " ")     
        print()

    def printAllRootToLeafPaths(self):
        root=self
        global vec
        if (not root):
            return
        vec.append(root.data)
        if (len(root.child) == 0):
            self.printPath(vec)
            vec.pop()
            return
        for i in range(len(root.child)):
            root.child[i].printAllRootToLeafPaths()       
        vec.pop()



### Test
root = Node('U235')
root.creaHijos()
for elemento in root.child:
    elemento.creaHijos()
root.printAllRootToLeafPaths()

# E^2 = (mc^2)^2 + (cp)^2

#########################################################
# Radon Decay: 222Rn -> 4He + 218Po
antes = ['Rn222']
despues = ['He4','Po218']
massDiff = diffMass(antes,despues) # Mev/c^2


####################################
# Fusiones
# D + D -> T + p        (1)
# D + D -> He3 + n      (2)

antes1 = ['H2','H2']
despues1 = ['He3','n']

dif1 = diffMass(antes1,despues1)

mD = massIsotope('H2')
mT = massIsotope('H3')
mHe3 = massIsotope('He3')
mp = massIsotope('p')
mn = massIsotope('n')

# D + D -> T + p        (1)
# D + D -> He3 + n      (2)

diff1 = 2*mD - mT - mp  
diff2 = 2*mD - mHe3 - mn


