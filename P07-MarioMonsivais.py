import matplotlib.pyplot as plt
import numpy as np

#Mario Monsivais 23-02-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P05-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P05-MarioMonsivais.py

#Definicion grafica
plt.title("Alcance Máximo")
plt.xlabel("x(m)")
plt.ylabel("y(m)")
plt.grid()


#Definicion de constantes
g = 9.81
beta = 4e-5
delta = 0.05
theta = 1.0
deltaT = 0.1
MaxA = -1.0
MaxF = -1.0

xf = []
yf = []

#Ciclo para cada angulo
while theta < 45.0:
    #Definicion de variables y arreglos
    t = 0
    v = 700

    x = 0
    vx = v*np.cos(theta*np.pi/180.0)
    xi = []

    y = 0
    vy = v*np.sin(theta*np.pi/180.0)
    yi = []

    #Euler
    while y > -0.05:
        x = x + vx*delta
        vx = vx - beta*v*vx*delta
        y = y + vy*delta
        vy = vy - g*delta - beta*v*vy*delta
        v = np.sqrt(vx**2 + vy**2)

        xi.append(x)
        yi.append(y)
    
    if MaxF < xi[-1]:
        MaxF = xi[-1]
        MaxA = theta
        xf = xi
        yf = yi
    theta += deltaT

#Graficacion
plt.plot(xf, yf, label="Aproximación θ= " + str(MaxA) + "°")

#Colocacion de leyendas y mostrar grafica
plt.legend(loc="upper right")
plt.show()