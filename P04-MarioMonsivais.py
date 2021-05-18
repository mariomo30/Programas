import matplotlib.pyplot as plt
import numpy as np

a = 10.0
b = 1.0
delta = 0.05
v = 0
t = 0
ti = []
vi = []
ti2 = np.arange(0, 30.0, 0.01)

while t < 30.0:
    v = v + (a - b*v)*delta
    t += delta
    vi.append(v)
    ti.append(t)

plt.title("Velocidad - tiempo")
plt.ylabel("v(m/s)")
plt.xlabel("t(s)")
plt.plot(ti2, (a - a*np.exp(-b*ti2)), 'blue', linewidth = 2, label="Analítica")
plt.plot(ti, vi, '--r', linewidth = 3, label="Aproximación")
plt.legend(loc="upper right")
plt.grid()
plt.show()