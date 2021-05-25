import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from mpl_toolkits.mplot3d import axes3d
import random
import math

N = 64
L = 20
T = 1
dt = 0.001
vx = np.zeros(N)
vy = np.zeros(N)

def pbcPosition(x, y, L):
    mx = math.fmod(x, L)
    my = math.fmod(y, L)
    if(mx < 0):
        mx -= L
    if(my < 0):
        my += L
    return mx, my

def pbcSeparation(ds, L):
    if(ds > 0.5*L):
        ds -= L
    else:
        ds += L
    return ds

def setVelocities(L, N):
    vxSum = 0.0
    vySum = 0.0
    for i in range(0, N):
        vx[i] = random.random() - 0.5
        vy[i] = random.random() - 0.5
        vxSum += vx[i]
        vySum += vy[i]
        
        vxcm = vxSum/N
        vycm = vySum/N
        v2sum = 0
        
    for j in range(0, N):
        vx[j] -= vxcm
        vy[j] -= vycm
        
    for k in range(0, N):
        v2sum += (vx[k]**2 + vy[k]**2)
    kipart = 1.0
    kpart = 0.5*v2sum/N
        
    rescale = (kipart/kpart)**0.5
        
    for i in range(0, N):
        vx[i] *= rescale
        vy[i] *= rescale
    return vx, vy

def setPositions(L, N):
    rx = np.array([])
    ry = np.array([])
    dx = L/8
    dy = L/8
    
    for i in range(0, 8):
        for j in range(0, 8):
            rx = np.append(rx, j+0.5)
            ry = np.append(ry, i+0.5)
    rx *= dx
    ry *= dy
    return rx, ry

def computeAcceleration(rx, ry, L, N):
    ax = np.zeros(len(x))
    ay = np.zeros(len(y))
    for i in range(0, len(x)):
        for j in range(i+1, len(x)):
            dx = pbcSeparation(rx[i] - rx[j], L)
            dy = pbcSeparation(ry[i] - ry[j], L)
            r2 = (dx**2 + dy**2)**0.5
            oneOverR2 = 1.0/r2
            fOverR = 24*(oneOverR2**2)*((2*oneOverR2**12) - (oneOverR2**6))
            fx = fOverR*dx
            fy = fOverR*dy
            ax[i] += fx
            ay[i] += fy
            ax[j] -= fx
            ay[j] -= fy
    return ax, ay

t = 0
re = 0
x, y = setPositions(L, N)

pos = []
pos.append(np.copy([x, y]))
Vx, Vy = setVelocities(L, N)
ax, ay = computeAcceleration(x, y, L, N)
temp = ([])
tiempo = ([])
kb = 1.3806*10**(-23)
while(t < 5):
    for i in range(0, len(x)):
        x[i] += (Vx[i]*dt) + ((ax[i])*(dt**2)/2)
        y[i] += (Vy[i]*dt) + ((ay[i])*(dt**2)/2)
        Vx[i] += (ax[i]*dt/2)
        Vy[i] += (ay[i]*dt/2)
        x[i], y[i] = pbcPosition(x[i], y[i], L)
    
    ax, ay = computeAcceleration(x, y, L, N)
    v2sum = 0
    for i in range(0, len(x)):
        Vx[i] += (ax[i]*dt/2)
        Vy[i] += (ay[i]*dt/2)
        v2sum += (Vx[i]**2 + Vy[i]**2)
    
    temp.append((2/(3*kb))*(0.5*v2sum/N))
    pos.append(np.copy([x, y]))
    t += dt
    tiempo.append(t)
    re += 1

plt.title("Temperatura - Tiempo")
plt.xlabel("Temperatura (k)")
plt.ylabel("Tiempo (s)")
plt.plot(tiempo, temp)
plt.grid()
plt.show()

def upd(n,fig, l,t):
    l.set_data(pos[n][0],pos[n][1])
    t.set_text('t = {:.2f} σ(m/ɛ)^(1/2)'.format(0.01*n))
    return l,t

def graficar(k,L,pos):
    fig, ax1 = plt.subplots(1,1,figsize=(9,9))
    text= plt.text(0.8,0.9,'matplotlib',horizontalalignment='center',verticalalignment='center',transform = ax1.transAxes)
    linea, = ax1.plot([],[],'r.')
    for ax in [ax1]:
        ax.set_ylim(0,L)
        ax.set_xlim(0,L)
        ax.grid()

    ax1.set_title("Movimiento de las partículas")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")

    line_ani = ani.FuncAnimation(fig, upd, frames=range(k), fargs=(fig,linea,text), repeat=True, interval=5, blit=True)
    plt.show()

graficar(re, L, pos)