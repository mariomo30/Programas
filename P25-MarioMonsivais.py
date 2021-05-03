import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import stats
import scipy.optimize
#Mario Monsivais 28-04-2021
#Instrucciones para correr:
#   Para Windows, en CMD colocarse en el directorio donde se encuentra el archivo y escribir: python P25-MarioMonsivais.py
#   Para Linux, en la terminal colocarse en el direcorio donde se encuentra el archivo y escribir: python P25-MarioMonsivais.py

def monoExp(x, m, t):
    return m * np.exp(t * x)

rn = np.zeros(20)
rn2 = np.zeros(20)
steps = np.zeros(20)

for j in range(1000):
    x, y = [0], [0]
    positions = set([0, 0])
    for i in range(20):
        deltas = [(1, 0), (0, 1), (-1, 0), (0,-1)]
        deltas_ok = []
        for dx, dy, in deltas:
            if( x[-1] + dx, y[-1] + dy) not in positions:
                deltas_ok.append((dx, dy))
        if deltas_ok:
            dx, dy = deltas_ok[random.randint(0,len(deltas_ok)-1)]
            positions.add((x[-1] + dx, y[-1] + dy))
            xi = x[-1] + dx
            yi = y[-1] + dy
            rn[i] = rn[i] + ((np.sqrt(xi**2 + yi**2))/100)
            rn2[i] = rn2[i] + ((xi**2 + yi**2)/100)
            steps[i] = i + 1
            x.append(x[-1] + dx)
            y.append(y[-1] + dy)
        else:
            break

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)
fig.suptitle("SAW 2-D.")

res1 = stats.linregress(steps, rn)
ax1.set_title("<$r$>")
ax1.set(xlabel="Número de pasos (Tiempo)", ylabel="<$r$>)")
ax1.plot(steps, rn, label="<$r$> - Tiempo")
ax1.plot(steps, res1.intercept + res1.slope*steps, 'r', label="Ajuste")
ax1.grid()

p0 = (10.0, .1)
params, cv = scipy.optimize.curve_fit(monoExp, steps, rn2, p0)
m, t = params
print(f"Y = {m} * e^({t} * x)")
ax2.set_title("<$r^2$>")
ax2.set(xlabel="Número de pasos (Tiempo)", ylabel="<$r^2$>")
ax2.plot(steps, rn2, label="<$r^2$> - Tiempo")
ax2.plot(steps, monoExp(steps, m, t), 'r', label="Ajuste")
ax2.grid()
plt.show()