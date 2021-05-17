import numpy as np
import matplotlib.pyplot as plt
import random

# Función para distancias
def dis(p0, p1):
    return np.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

# Indices
n1 = 1.0
n2 = 1.5

# Punto inicial
x0 = 0
y0 = 0

# Punto final
xf = 2.0 
yf = 0.7

# x intermedias
x = [0.25, 0.50, 0.75, 1.0, 1.25, 1.50, 1.75]

# y aleatorias
y = []
for i in range(7):
    y.append(np.random.uniform(0, 1))

d = 0.1

# LCO
delta = 0.005

# Función calculo de LCOi
def ProcLCOi(P0, P1, P2, idx):
    LCO_Back = dis((P0[0], P0[1]), (P1[0], P1[1]))
    LCO_Front = dis((P1[0], P1[1]), (P2[0], P2[1]))

    if idx == 3:
        LCO_Back = LCO_Back*n1 
        LCO_Front = LCO_Front*n2   
    elif(idx > 3):
        LCO_Back = LCO_Back*n2
        LCO_Front = LCO_Front*n2
    else:
        LCO_Back = LCO_Back*n1
        LCO_Front = LCO_Front*n1

    return (LCO_Front + LCO_Back)

# Método Variacional
LCO = 0
k = 300
for i in range(k):
    idx = random.randint(1, 5)
    P0 = (x[idx-1], y[idx-1])
    P1 = (x[idx], y[idx])
    P2 = (x[idx+1], y[idx])

    LCOI = ProcLCOi(P0, P1, P2, idx)
    yn = y[idx]

    while True:
        r = 2*random.randint(0, 1) - 1
        yn = yn + d*r
        P1 = (x[idx], yn)
        LCON = ProcLCOi(P0, P1, P2, idx)

        if LCON <= LCOI and abs(LCON - LCOI) <= delta:
            LCOI = LCON
            y[idx] = yn
            break

plt.plot(x, y)
plt.show()