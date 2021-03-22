import matplotlib.pyplot as plt
import numpy as np

#Mario Monsivais 18-03-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P14-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P14-MarioMonsivais.py

plt.figure(figsize=(5,5))
plt.plot(0, 0, 'yo', label="Sol")
plt.xlabel('x (UA)')
plt.ylabel('y (UA)')
plt.title('x vs y')

ri = [0.72, 1.00, 1.52, 5.20, 9.54]
mi = [4.9e24, 6.0e24, 6.6e23, 1.9e27, 5.7e26]
Ti = [0.614, 1, 1.88, 11.86, 29.5]
p = ['Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno']
c = ['brown', 'blue', 'red', 'orange', 'purple']
i = 0

for r in ri:
    x = r
    y = 0

    vx = 0
    vy = 2*np.pi

    xi = []
    yi = []
    t = 0
    dt = 0.0001
    v = 0

    while t < r:
        x = x + vx*dt
        vx = vx - (4*(np.pi**2)*x*dt/(r**2))
        y = y + vy*dt
        vy = vy - (4*(np.pi**2)*y*dt/(r**2))
        t += dt
        xi.append(x)
        yi.append(y)
        v = np.sqrt(vx**2 + vy**2)
    plt.plot(xi,yi, color=c[i], label="Orbita de" + p[i])
    print(p[i], Ti[i]**2/r**3)
    i+=1

plt.legend(loc="upper right")
plt.grid()
plt.show() 