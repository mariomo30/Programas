import matplotlib.pyplot as plt
import numpy as np

#Mario Monsivais 29-03-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P18-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P18-MarioMonsivais.py

ms = 2.0e30
me = 6.0e24
mm = 7.3e22

MMS = mm/ms
MES = me/ms

dt = 0.0001
G = 4*(np.pi**2)

t = 0

xe = 1
ye = 0

xm = 1.0026
ym = 0

vxe = 0
vye = 2*np.pi

vxm = 0
vym = vye + (2*np.pi*0.0026/0.14)

xie = []
yie = []

xim = []
yim = []

while t < 1:
    re = np.sqrt(xe**2 + ye**2)
    rm = np.sqrt(xm**2 + ym**2)
    rem = 0.0026

    vxe = vxe - ((G*xe)/(re**3))*dt - ((G*MMS*(xe - xm))/(rem**3))*dt
    vye = vye - ((G*ye)/(re**3))*dt - ((G*MMS*(ye - ym))/(rem**3))*dt

    vxm = vxm - ((G*xm)/(rm**3))*dt - ((G*MES*(xm - xe))/(rem**3))*dt
    vym = vym - ((G*ym)/(rm**3))*dt - ((G*MES*(ym - ye))/(rem**3))*dt

    xe = xe + vxe*dt
    ye = ye + vye*dt

    x = 0.0026
    y = 0

    vx = 0
    vy = (2*np.pi*0.0026/0.14)

    r = ((xm**2)+(ym**2))**(0.5)
    xm = xm + vx*dt
    vx = vx - (4*((np.pi)**2)*xm*dt/(r**3))
    ym = ym + vym*dt
    vy = vy - (4*((np.pi)**2)*ym*dt/(r**3))

    xm = xm + vxm*dt
    ym = ym + vym*dt

    xie.append(xe)
    yie.append(ye)

    xim.append(xm)
    yim.append(ym)

    t += dt

plt.figure(figsize=(5,5))
plt.plot(xie,yie, color='blue', label="Orbita de la Tirra")
plt.plot(xim,yim, color='red', label="Orbita de la Luna")
plt.plot(0, 0, 'yo', label="Sol")
plt.xlabel('x (UA)')
plt.ylabel('y (UA)')
plt.title('x vs y')
plt.legend(loc="upper right")
plt.grid()
plt.show() 