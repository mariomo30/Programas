import matplotlib.pyplot as plt
import numpy as np

v = 40
t = 0
x = 0
t = 0
delta = 0.05
xi = []
ti = []
ti2 = np.arange(0.0, 100.0, 0.05)

while t < 100:
    x = x + v*delta
    t += delta
    xi.append(x)
    ti.append(t)

plt.title("Posición - tiempo")
plt.plot(ti, xi, '--r', linewidth = 3, label="Aproximación")
plt.plot(ti2, v*ti2, 'b', label="Analítica")
plt.ylabel("x(m)")
#plt.xlim([-1,12])
plt.xlabel("t(s)")
#plt.ylim([-10, 500])
plt.legend(loc="upper right")
plt.grid()
plt.show()