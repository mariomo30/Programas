import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import stats

#Mario Monsivais 29-03-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P18-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P18-MarioMonsivais.py

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)
fig.suptitle("Caminata aleatoria 2-D.")
ax1.set_title("Caminatas aleatorias.")
ax1.set(xlabel="x(m)", ylabel="y(m)")
ax1.grid()
ax2.set_title("Promedio de desplazamiento")
ax2.set(xlabel="Número de pasos (Tiempo)", ylabel="<$r^2$>")
ax2.grid()


#Direcciones
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
r = np.zeros(20)
steps = np.zeros(20)

#Caminatas
for j in range(0, 5):

    #Caminata
    x = 0
    y = 0
    xi = []
    yi = []

    for i in range(0, 20):
        steps[i] = i+1
        dr = random.randint(0, 3)
        x = x + dx[dr]
        y = y + dy[dr]
        r[i] += ((np.sqrt(x**2 + y**2))/100)
        xi.append(x)
        yi.append(y)

    ax1.plot(xi, yi, label="Caminata " + str(i))

res = stats.linregress(steps, r)
ax2.plot(steps, r, label="<$r^2$> - Tiempo")
ax2.plot(steps, res.intercept + res.slope*steps, 'r', label="Ajuste")
plt.show()

#plt.xlim(-10, 110)
#plt.ylim(-10, 110)
#plt.title("Caminata aleatoria en una dimensión")
#plt.ylabel("<$r^2$>")
#plt.xlabel("Número de pasos (Tiempo)")
#plt.plot(steps, r, label="<$r^2$> - Tiempo")
#plt.plot(steps, res.intercept + res.slope*steps, 'r', label="Ajuste")
#plt.grid()
#plt.legend()
#3plt.show()