import matplotlib.pyplot as plt
import numpy as np

#Mario Monsivais 22-02-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P05-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P05-MarioMonsivais.py

#Definicion graficas
fig, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True)
ax1.set_title("Altura - Alcance")
ax1.set(xlabel="x(m)", ylabel="y(m)")
ax1.grid()
ax2.set_title("Velocidad - Tiempo")
ax2.set(xlabel="t(s)", ylabel="v(m/s)")
ax2.grid()

#Definicion de constantes
g = 9.81
delta = 0.05
thetas = [10, 20, 30, 40, 50, 60, 70, 80, 90]

#Ciclo para cada angulo
for theta in thetas:
    #Definicion de variables y arreglos
    t = 0
    ti = []
    v = 700
    vi = []

    x = 0
    vx = v*np.cos(theta*np.pi/180.0)
    xi = []

    y = 0
    vy = v*np.sin(theta*np.pi/180.0)
    yi = []

    #Euler
    while y > -0.05:
        x = x + vx*delta
        vx = vx
        y = y + vy*delta
        vy = vy - g*delta
        t += delta

        ti.append(t)
        xi.append(x)
        yi.append(y)
        vi.append(np.sqrt(vx**2 + vy**2))
    #Graficacion
    ax1.plot(xi, yi, label="Aproximación θ= " + str(theta) + "°")
    ax2.plot(ti, vi, label="Aproximación θ= " + str(theta) + "°")

#Colocacion de leyendas y mostrar grafica
ax1.legend(bbox_to_anchor=(1.1, 1.05))
ax2.legend(bbox_to_anchor=(1.1, 1.05))
plt.show()