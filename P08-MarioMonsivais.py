import matplotlib.pyplot as plt
import numpy as np

#Mario Monsivais 29-02-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P08-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P08-MarioMonsivais.py

#Definicion grafica
plt.title("Péndulo")
plt.xlabel("t(s)")
plt.ylabel("Theta(°)")
plt.grid()


#Definicion de constantes y diccionarios
g = 9.81
l = 1.0
ti = []
wi = []
thetai = []
w = 0
t = 0
theta = 10
delta = 0.05

thetan = 10
wn = 0
wnf = 0
tnf = 0
thetani = []
wni = []

#Metodo de Euler
while t < 10.0:
    wnf = wn - (g/l)*thetan*delta
    tnf = thetan + wn*delta
    
    w = w - (g/l)*theta*delta
    theta = theta + w*delta
    t += delta

    ti.append(t)
    wi.append(w)
    thetai.append(theta)
    thetani.append(tnf)
    wni.append(wnf)
    wn = wnf
    thetan = tnf

#Graficacion
plt.plot(ti, thetai, label="Aproximación buena")
plt.plot(ti, thetani, label="Aproximación mala")
#Colocacion de leyendas y mostrar grafica
plt.legend(loc="upper right")
plt.show()