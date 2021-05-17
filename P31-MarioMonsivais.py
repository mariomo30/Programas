import numpy as np
import matplotlib.pyplot as plt
import random

# Función para distancia entre dos puntos
def dis(p0, p1):
    return np.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

# Funcion para calcular LCO total (Completo)
def ProcLCO(x, y):
    LCO = 0
    for i in range(8):
        p1 = (x[i], y[i])
        p2 = (x[i+1], y[i+1])

        if i >= 4:
            LCO += dis(p1, p2)*n2
        else:
            LCO += dis(p1, p2)*n1

    return LCO

# Indices
n1 = 1.0
n2 = 1.5

# x intermedias
x = [0, 0.25, 0.50, 0.75, 1.0, 1.25, 1.50, 1.75, 2.0]

# y aleatorias intermedias
y = []
for i in range(9):
    y.append(np.random.uniform(0, 1))
y[0] = 0
y[-1] = 0.7

# variación en y
d = 0.01

# Condición de cambio
delta = 0.0005

# Método Variacional
k = 1000

for i in range(k):
    idx = random.randint(1, 7) # Punto aleatorio

    LCOI = ProcLCO(x, y) # LCO inicial
    LCON = 0

    while True:
        r = 2*random.randint(0, 1) - 1 # 'r' entre -1 y 1
        y[idx] = y[idx] + d*r # Calculo de la y nueva

        LCON = ProcLCO(x, y) # claculo de la nueva LCOi

        # Verificar si es minimo este LCO nuevo
        if LCON <= LCOI or abs(LCOI - LCON) <= delta:
            break
    print(i)

# Calculamos LCO para ver si se cumple la ley de Snell
pm = () # Punto en l

# Dibujando materiales
plt.plot((0, 0), (0, 1), c='red')
plt.plot((0, 1), (1, 1), c='red')
plt.plot((1, 1), (0, 1), c='red')
plt.plot((0, 1), (0, 0), c='red')

plt.plot((1, 1), (0, 1), c='blue')
plt.plot((1, 2), (1, 1), c='blue')
plt.plot((2, 2), (0, 1), c='blue')
plt.plot((1, 2), (0, 0), c='blue')

# Resultado
plt.title("Mínimo LCO calculado")
plt.grid()
plt.plot(x, y, c='black', label="LCO aproximado")
plt.legend(loc='best')
plt.show()