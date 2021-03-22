import matplotlib.pyplot as plt
import numpy as np

#Mario Monsivais 18-03-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P14-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P14-MarioMonsivais.py

x = 1
y = 0

vx = 0
vy = 2*np.pi

xi = []
yi = []
t = 0
dt = 0.0001
r=(x**2+y**2)**(0.5)

while t < 1:
    r = ((x**2)+(y**2))**(0.5)
    x = x + vx*dt
    vx = vx - (4*((np.pi)**2)*x*dt/(r**3))
    y = y + vy*dt
    vy = vy - (4*((np.pi)**2)*y*dt/(r**3))
    t += dt
    xi.append(x)
    yi.append(y)

plt.figure(figsize=(5,5))
plt.plot(xi,yi, color='xkcd:purple', label="Orbita de la tirra")
plt.plot(0, 0, 'yo', label="Sol")
plt.xlabel('x (UA)')
plt.ylabel('y (UA)')
plt.title('x vs y')
plt.legend(loc="upper right")
plt.grid()
plt.show() 