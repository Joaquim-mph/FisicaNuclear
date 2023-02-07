import numpy as np 
import matplotlib.pyplot as plt

archivo = 'StandardSolarModel.txt'

def cargar(archivo):
        M   = []
        R   = []
        T   = []
        Rho = []
        P   = []
        L   = []
        X   = []
        Y   = []
        He3 = []
        C12 = []
        N14 = []
        O16 = []
        Archivo = open(archivo, "r")
        k=0
        for linea in Archivo:
            k += 1
            if k > 23 and k < 1095:
                linea = linea.strip()
                lista = linea.split("  ") 
                M.append(float(lista[0]))
                R.append(float(lista[1]))
                T.append(float(lista[2]))
                Rho.append(float(lista[3]))
                P.append(float(lista[4]))
                L.append(float(lista[5]))
                X.append(float(lista[6]))
                Y.append(float(lista[7]))
                He3 .append(float(lista[8]))
                C12.append(float(lista[9]))
                N14.append(float(lista[10]))
                O16.append(float(lista[11]))
        Archivo.close()
        return M, R, T, Rho, P, L, X, Y, He3, C12, N14, O16

M, R, T, Rho, P, L, X, Y, He3, C12, N14, O16 = cargar(archivo)

#Vectores con los integrados discretos#

rhoR = []
for i in range(len(M)):
    rhoR.append(Rho[i]*R[i])

rhoRsquared = []
for i in range(len(M)):
    rhoRsquared.append(Rho[i]*R[i]**2)

rhoRquartic = []
for i in range(len(M)):
    rhoRquartic.append(Rho[i]*R[i]**4)

# Integral <-> Suma por trapecios de numpy

Up = np.trapz(rhoRquartic,R)
Up2 = np.trapz(rhoR,R)
Down = np.trapz(rhoRsquared,R)

meanRSquare = np.sqrt(Up/Down) # 0.3313294875161024
meanR = Up2/Down
XY = []
for i in range(len(M)):
    XY.append(X[i]+Y[i])

plt.clf()
plt.plot(R,M,label='Density')
#plt.plot(R,Y,label='He4')
#plt.plot(R,XY)
plt.legend()
plt.show()

### Calculo numerico a mano (Sin Libreria) ###

#Numerador, integral de rhoRquartic#

Iup = 0

for i in range(len(R)-1):
    Iup += (R[i+1] - R[i])*(rhoRquartic[i] + rhoRquartic[i+1])/2

#Denominador, integral de rhoRsquared#

Idown = 0

for i in range(len(R)-1):
    Idown += (R[i+1] - R[i])*(rhoRsquared[i] + rhoRsquared[i+1])/2

rootMean = np.sqrt(Iup/Idown)

print(rootMean)