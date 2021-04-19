import matplotlib.pyplot as plt
import numpy as np

#Mario Monsivais 23-03-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P16-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P16-MarioMonsivais.py

ms = 2.0e30
me = 6.0e24
mj = 1.9e27
dt = 0.0001
G = 4*(np.pi**2)
MJS = mj/ms
MES = me/ms
t = 0

xe = 1
ye = 0

xj = 5.20
yj = 0

vxe = 0
vye = 2*np.pi

vxj = 0
vyj = 2*np.pi*5.20/11.86

xie = []
yie = []

xij = []
yij = []

while t < 11.86:
    re = np.sqrt(xe**2 + ye**2)
    rj = np.sqrt(xj**2 + yj**2)
    rej = np.sqrt((xe - xj)**2 + (ye - yj)**2)

    vxe = vxe - ((G*xe)/(re**3))*dt - ((G*MJS*(xe - xj))/(rej**3))*dt
    vye = vye - ((G*ye)/(re**3))*dt - ((G*MJS*(ye - yj))/(rej**3))*dt

    vxj = vxj - ((G*xj)/(rj**3))*dt - ((G*MES*(xj - xe))/(rej**3))*dt
    vyj = vyj - ((G*yj)/(rj**3))*dt - ((G*MES*(yj - ye))/(rej**3))*dt

    xe = xe + vxe*dt
    ye = ye + vye*dt

    xj = xj + vxj*dt
    yj = yj + vyj*dt

    xie.append(xe)
    yie.append(ye)

    xij.append(xj)
    yij.append(yj)

    t += dt

plt.figure(figsize=(5,5))
plt.plot(xie,yie, color='blue', label="Orbita de la tirra")
plt.plot(xij,yij, color='red', label="Orbita de jupiter")
plt.plot(0, 0, 'yo', label="Sol")
plt.xlabel('x (UA)')
plt.ylabel('y (UA)')
plt.title('x vs y')
plt.legend(loc="upper right")
plt.grid()
plt.show() 