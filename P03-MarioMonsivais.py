import matplotlib.pyplot as plt
import numpy as np

g = 9.81
deltas = [0.05, 0.1, 0.5, 1]
ti2 = np.arange(0.0, 10.0, 0.05)
color = ["--r", "--b", "--g", "--s"]
i = 0
plt.title("Velocidad - tiempo")
plt.ylabel("v(m/s)")
plt.xlabel("t(s)")
plt.plot(ti2, -g*ti2, 'pink', label="Analítica")

for delta in deltas:
    vi = []
    ti = []
    v = 0
    t = 0
    while t < 10.0:
        v = v - g*delta
        t += delta
        vi.append(v)
        ti.append(t)
    plt.plot(ti, vi, color[i], linewidth = 3, label="Aproximación delta = " + str(delta))
    i+=1
plt.legend(loc="upper right")
plt.grid()
plt.show()