import numpy as np

file1 = open("MyFile.txt","r")
a = file1.readlines()
file1.close()

x = np.zeros(10)
y = np.zeros(10)

r = [(0, 0.1), (0.1, 0.2), (0.2, 0.3), (0.3, 0.4), (0.4, 0.5), (0.5, 0.6), (0.6, 0.7), (0.7, 0.8), (0.8, 0.9), (0.9, 1)]

for i in range(len(r)):
    for j in range(len(a)):
        f = float(a[j])
        if f > r[i][0] and f <= r[i][1]:
            x[i] += 1
    y[i] = 10

x2 = 0

for i in range(10):
    x2 += ((x[i] - y[i])**2)/y[i]

print("Valor de la chi2 = " + str(x2))
