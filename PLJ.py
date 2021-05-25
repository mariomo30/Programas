import numpy as np
import matplotlib.pyplot as plt

def f(r):
    epsilon = 0.0103
    sigma = 3.4
    return (24 * epsilon / r) * ( 2*np.power((sigma / r), 12) - np.power((sigma / r), 6) )

def u(r):
    epsilon = 0.0103
    sigma = 3.4
    return (4 * epsilon) * ( np.power((sigma / r), 12) - np.power((sigma / r), 6) )

r = np.linspace(3.5, 8, 100)
r1 = np.linspace(2.7, 8, 100)

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)

ax1.plot(r, f(r))
ax1.set_title("Magnitud de la fuerza")
ax1.set(ylabel = "$f(r)/Å$")
ax1.set(xlabel = "$r/Å$")
ax1.grid()

ax2.plot(r, u(r1))
ax2.scatter(2.74, u(2.74))
ax2.set_title("Potencial de Lennar - Jones")
ax2.set(ylabel = "$u(r)/Å$")
ax2.set(xlabel = "$r/Å$")
ax2.grid()

plt.show()