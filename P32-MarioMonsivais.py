import numpy as np
import matplotlib.pyplot as plt
import time

def mod(a, b):
    return a % b

print("Resultados del inciso a):")
print("10.2 % 3.3 = ",mod(10.2, 3.3))
print("-10.2 % 3.3 = ",mod(-10.2, 3.3))
print("10.2 % -3.3 = ",mod(10.2, -3.3))
print("-10.2 % -3.3 = ",mod(-10.2, -3.3))


def pbcPosition(s, L):
    s = s % L
    return s % L + L if s < 0 else s % L



print("Resultados del inciso b):")
print("-17 % 5 =",pbcPosition(-17, 5))

def pbcPosition_Last(s, L):
    if s > L:
        s -= L
    else:
        s += L
    return s

def checkTime():
    n = 1000000
    test = []
    for i in range(n):
        test.append([(-1**i)*np.random.random(), np.random.random()])

    start_time = time.time()
    for i in range(n):
        pbcPosition(test[i][0], test[i][1])
    print("Versión con el operador %:", time.time() - start_time, "segundos")

    start_time = time.time()
    for i in range(n):
        pbcPosition_Last(test[i][0], test[i][1])
    print("Versión sin el operador %:", time.time() - start_time, "segundos")
    
print("Resultados del inciso c):")
checkTime()