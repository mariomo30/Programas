import matplotlib.pyplot as plt
import numpy as np

#Definicion graficas
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True)
ax1.set_title("Vs - Tiempo")
ax1.set(xlabel="t(s)", ylabel="Vs(v)")
ax1.grid()
ax2.set_title("Vr - Tiempo")
ax2.set(xlabel="t(s)", ylabel="Vr(v)")
ax2.grid()
ax3.set_title("Vc - Tiempo")
ax3.set(xlabel="t(s)", ylabel="Vc(v)")
ax3.grid()

R = 1000
C = 1e-6
fi = [10, 50, 100, 160, 200, 500, 1000, 5000, 10000]

for f in fi:
    s = "Aproximación f= " + str(f) + "Hz"
    delta = 0.0001
    q = 0
    qi = []
    vr = []
    vc = []
    vs = []
    t = 0.0
    ti = []

    if f == 10000:
        delta = 0.000001
        s += " con delta = 0.000001 "

    while t < 0.006:
        vsi = np.cos(2*np.pi*f*t)
        vs.append(vsi)
        vr.append(vsi - q/C)
        vc.append(q/C)
        q = q + (vsi/R - (q/(R*C)))*delta
        t += delta
        ti.append(t)

    #Graficacion
    ax1.plot(ti, vs, label = s)
    ax2.plot(ti, vr)
    ax3.plot(ti, vc)

ax1.legend(bbox_to_anchor=(1.1, 1.05))
plt.show()