import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import stats

#Mario Monsivais 29-03-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P18-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P18-MarioMonsivais.py

#Direcciones
dx = [-1, 1]
r = np.zeros(100)
steps = np.zeros(100)

#Caminatas
for j in range(0, 100):

    #Caminata
    x = 0
    steps[j] = j+1
    for i in range(0, 100):
        dr = random.randint(0, 1)
        x = x + dx[dr]
        r[i] += (((x/(j+1))**2)/100)

res = stats.linregress(steps, r)

plt.xlim(-10, 110)
plt.ylim(-10, 110)
plt.title("Caminata aleatoria en una dimensión")
plt.ylabel("<$x^2$>")
plt.xlabel("Número de pasos (Tiempo)")
plt.plot(steps, r, label="<$x^2$> - Tiempo")
plt.plot(steps, res.intercept + res.slope*steps, 'r', label="Ajuste")
plt.grid()
plt.legend()
plt.show()