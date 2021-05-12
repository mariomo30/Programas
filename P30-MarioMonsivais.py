import numpy as np
import matplotlib.pyplot as plt

xInside = []
yInside = []
xOutside = []
yOutside = []
area = 0
out = 0
n = 0

while True:
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)

    r = np.sqrt(x**2  + y**2)

    if r <= 1.0:
        xInside.append(x)
        yInside.append(y)
        area += 1
    else:
        xOutside.append(x)
        yOutside.append(y)
        out += 1
    n += 1
    pi = 4*(area/n)

    if str(pi) == "3.1415":
        break
    if str(round(pi, 4)) == "3.1415":
        pi = round(pi, 4)
        break
    if n == 4000000:
        break
    
lab = "Área de la porción del círculo = " + str(pi/4) + " $u^2$"

X = np.linspace(0, 1.0, 100)
Y = np.sqrt(1 - X**2)

plt.figure(figsize = (5,5))
plt.title("Aproximación de $\pi$ = " + str(pi) + " con n = " + str(n))
plt.scatter(xInside, yInside, c = 'red', s = 1, label = lab)
plt.scatter(xOutside, yOutside, c = 'blue', s = 1, label = "Puntos rechazados")
plt.plot(X, Y, c="black", linewidth=2)
plt.legend(loc="upper left")
plt.grid()
plt.show()