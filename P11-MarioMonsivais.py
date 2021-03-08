import matplotlib.pyplot as plt
import numpy as np

#Mario Monsivais 08-03-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P11-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P11-MarioMonsivais.py

#Definicion grafica
plt.title("Péndulo (Euler - Cromer)")
plt.xlabel("t(s)")
plt.ylabel("Theta(radians)")
plt.grid()


#Definicion de constantes y diccionarios
g = 9.81
l = 1.0
delta = 0.05
q = 1
ti = []
wi = []
thetai = []
w = 0.0
theta = 10*(np.pi/180.0)
t = 0
Fd = 0.2
wd = 2.0

#Metodo de Euler
while t < 20.0:
    ti.append(t)
    wi.append(w)
    thetai.append(theta)
    t += delta
    w = w - (g/l)*theta*delta - q*w*delta + Fd*np.sin(wd*t)*delta
    theta = theta + w*delta

#Graficacion
plt.plot(ti, thetai, label="Ángulo de resonancia en \u03B8 = " + str(10.0) + "°")

#Colocacion de leyendas y mostrar grafica
plt.legend(loc="upper right")
plt.show()
