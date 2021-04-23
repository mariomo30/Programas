import matplotlib.pyplot as plt
import random
import numpy as np
import random
#Mario Monsivais 22-04-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P24-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P24-MarioMonsivais.py

def SAW(n):
    x, y = [0], [0]
    positions = set([0, 0])
    for i in range(n):
        deltas = [(1, 0), (0, 1), (-1, 0), (0,-1)]
        deltas_ok = []
        for dx, dy, in deltas:
            if( x[-1] + dx, y[-1] + dy) not in positions:
                deltas_ok.append((dx, dy))
        if deltas_ok:
            dx, dy = deltas_ok[random.randint(0,len(deltas_ok)-1)]
            positions.add((x[-1] + dx, y[-1] + dy))
            x.append(x[-1] + dx)
            y.append(y[-1] + dy)
        else:
            break
    return x, y

plt.title("SAW")
for i in range(5):
    x, y = SAW(20)
    plt.plot(x, y, label="Caminata" + str(i+1))

plt.xlabel("X(m)")
plt.ylabel("Y(m)")
plt.legend()
plt.grid()
plt.show()