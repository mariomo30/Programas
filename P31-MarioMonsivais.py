import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

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

# Punto inicial
Pi = (0, 0)
# Punto final
Pf = (2.0, 0.7)

# 'x' intermedias
x = [0, 0.25, 0.50, 0.75, 1.0, 1.25, 1.50, 1.75, 2.0]

# 'y' aleatorias intermedias
y = []
for i in range(9):
    y.append(np.random.uniform(0, 1))
y[0] = 0
y[-1] = 0.7

# variación en 'y'
d = 0.01

# Condición de cambio
delta = 0.0005

# Método Variacional
k = 1000
fig, ax = plt.subplots()
ax = plt.axes()
ax.set_ylim(0, 1.1)
ax.set_xlim(0, 2.1)
cY = []

for i in range(k):
    idx = random.randint(1, 7) # Punto aleatorio

    LCOI = ProcLCO(x, y) # LCO inicial
    LCON = 0

    while True:
        r = 2*random.randint(0, 1) - 1 # 'r' entre -1 y 1
        y[idx] = y[idx] + d*r # Calculo de la 'y' nueva
        if y[idx] >= 1 or y[idx] <= 0:
            y[idx] = 0.5
        LCON = ProcLCO(x, y) # claculo de la nueva LCOi

        # Verificar si es minimo este LCO nuevo o si el cambio es menor al delta
        if LCON < LCOI or abs(LCOI - LCON) <= delta:
            break
    cY.append(y.copy())
    print(((i+1)/10), "%") # Mostrando porcentaje de simulación

# Animación
line, = ax.plot(x, cY[0])
def anime(i):
    line.set_ydata(cY[i])
    return line,

anim = animation.FuncAnimation(fig, func=anime, frames=1000, interval=0.1, repeat=False)

# Calculamos LCO para ver si se cumple la ley de Snell
Pm = (x[4], y[4]) # Punto en la interfaz

n1sent1 = n1*Pm[1]/dis(Pi, Pm)
n2sent2 = n2*(Pf[1] - Pm[1])/dis(Pm, Pf)

print("Para n1", n1sent1)
print("Para n2", n2sent2)
# Dibujando materiales
# N1
plt.plot((0, 0), (0, 1), c='red', label="$n_1$ = 1.0")
plt.plot((0, 1), (1, 1), c='red')
plt.plot((1, 1), (0, 1), c='red')
plt.plot((0, 1), (0, 0), c='red')

# N2
plt.plot((1, 1), (0, 1), c='blue', label = "$n_2$ = 1.5")
plt.plot((1, 2), (1, 1), c='blue')
plt.plot((2, 2), (0, 1), c='blue')
plt.plot((1, 2), (0, 0), c='blue')

# Resultado
plt.title("Mínimo LCO calculado,\n $n_1*sin(\\theta_1)=$" + str(n1sent1) + ", $n_2*sin(\\theta_2)=$" + str(n2sent2) + "\n $n_1*sin(\\theta_1) \u2248 n_2*sin(\\theta_2)$")
plt.grid()
plt.plot(x, y, c = 'black', label = " LCO aproximado")
plt.plot((Pi[0], Pm[0], Pf[0]), (Pi[1], Pm[1], Pf[1]), c = 'green', linestyle = "--", label = "LCO real")
plt.legend(loc = 'best')
plt.show()
