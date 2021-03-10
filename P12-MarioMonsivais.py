import matplotlib.pyplot as plt
import numpy as np

#Mario Monsivais 09-03-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P12-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P12-MarioMonsivais.py

#Definicion grafica
plt.title("Péndulo (Euler - Cromer)")
plt.xlabel("t(s)")
plt.ylabel("Theta(radians)")
plt.grid()


#Definicion de constantes y diccionarios
g = 9.81
l = 1.0
ti = []
wi = []
thetai = []
w = 0.0
theta = 20*(np.pi/180.0)
delta = 0.05
t = 0

#Metodo de Euler
while t < 10.0:
    w = w - (g/l)*np.sin(theta)*delta
    theta = theta + w*delta
    t += delta

    ti.append(t)
    wi.append(w)
    thetai.append(theta)

#Graficacion
plt.plot(ti, thetai, label="Aproximación en \u03B8 = 20°")
#Colocacion de leyendas y mostrar grafica
plt.legend(loc="upper right")
plt.show()