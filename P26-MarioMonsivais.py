import math
import matplotlib.pyplot as plt
import numpy as np
import random


n = 50
m = 500
l = 20000
nprom = 0
H = np.zeros(n)

for k in range(l):
    tab = np.random.randint(0, n, m)
    h = np.zeros(n)
    for i in range(n):
        if k == 0:
            nprom += tab[i]/n
        h[tab[i]] += 1

    for i in range(n):
        H[i] += h[i]/m

p = []
dardos = np.zeros(n)
for i in range(n):
    p.append(H[i]/m)
    dardos[i] = i

P = np.zeros(n)
for i in range(n):
    P[i] = ((nprom**i)/(math.factorial(i)))*(np.exp(-nprom))

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)
fig.suptitle("Dardos")

ax1.hist(p)
ax1.grid()
ax2.plot(dardos, P)
ax2.grid()
plt.show()


