import matplotlib.pyplot as plt
import numpy as np

Nt = np.zeros(100)
ti = np.zeros(100)

for k in range(100):
    ti[k] = k
    p = 0.001
    Ni = 10000
    dt =  1
    Ne = 0
    t = 0

    while t < 100:
        N_in = 0
        N_es = 0
        for i in range(Ni):
            r = np.random.uniform(0, 1)
            if r <= p:
                N_in = N_in + 1
                N_es = N_es + 1
        
        Ni = Ni - N_in
        Ne = Ne + N_es
        Nt[t] += Ni/100
        t += dt

plt.plot(ti, Nt)
plt.grid()
plt.show()