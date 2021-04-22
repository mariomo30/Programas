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
ax1.set_title("Promedio de desplazamiento")
ax1.set(xlabel="Número de pasos (Tiempo)", ylabel="<r>")
ax1.grid()
ax2.set_title("Promedio de desplazamiento al cuadrado")
ax2.set(xlabel="Número de pasos (Tiempo)", ylabel="<$r^2$>")
ax2.grid()


#Direcciones
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
r = np.zeros(20)
r2 = np.zeros(20)
steps = np.zeros(20)

#Caminatas
for j in range(0, 100):

    #Caminata
    x = 0
    y = 0

    for i in range(0, 20):
        steps[i] = i+1
        dr = random.randint(0, 3)
        x = x + dx[dr]
        y = y + dy[dr]
        r2[i] += ((np.sqrt(x**2 + y**2))/100)
        r[i] += ((x**2 + y**2)/100)

res = stats.linregress(steps, r)
res2 = stats.linregress(steps, r2)
ax1.plot(steps, r, label="<r> - Tiempo")
ax1.plot(steps, res.intercept + res.slope*steps, 'r', label="Ajuste")
ax2.plot(steps, r2, label="<$r^2$> - Tiempo")
ax2.plot(steps, res2.intercept + res2.slope*steps, 'r', label="Ajuste")
plt.show()
