import matplotlib.pyplot as plt
import numpy as np

#Mario Monsivais 05-03-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P10-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P10-MarioMonsivais.py

#Definicion grafica
plt.title("Péndulo (Euler - Cromer)")
plt.xlabel("t(s)")
plt.ylabel("Theta(°)")
plt.grid()


#Definicion de constantes y diccionarios
g = 9.81
l = 1.0
delta = 0.05
qi = [1, 5, 10]

#Ciclo para cada q
for q in qi:
    ti = []
    wi = []
    thetai = []
    w = 0.0
    theta = 10
    t = 0

    #Metodo de Euler
    while t < 10.0:
        w = w - (g/l)*theta*delta -q*w*delta
        theta = theta + w*delta
        t += delta
        ti.append(t)
        wi.append(w)
        thetai.append(theta)

    #Graficacion
    plt.plot(ti, thetai, label="Aproximación q = " + str(q))

#Colocacion de leyendas y mostrar grafica
plt.legend(loc="upper right")
plt.show()
