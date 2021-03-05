import matplotlib.pyplot as plt
import numpy as np

Nu = 100.0
t = 0
tao = 1.0
delta = 0.05
Ni = []
ti = []

while Nu > 0.001:
    Nu = Nu*(1.0 - (delta/tao))
    t += delta
    Ni.append(Nu)
    ti.append(t)

ti2 = np.arange(0.0, 15.0, 0.05)
plt.title("Gráfica de decaimiento radioactivo")
plt.plot(ti, Ni, '--r', linewidth = 3, label="Aproximación")
plt.plot(ti2, 100*np.exp(-ti2), 'b', label="Analítica")
plt.ylabel("Nu(t)")
plt.xlim([-1,15])
plt.xlabel("t(s)")
plt.ylim([-10, 110])
plt.legend(loc="upper right")
plt.grid()
plt.show()