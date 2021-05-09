import matplotlib.pyplot as plt

r0 = 1234
a = 106
c = 1283
m = 6075

# Primer punto
ri = r0
r = []
si = []
file1 = open("MyFile.txt","a")
for i in range(100):
    ri = (a*ri + c) % m 
    r.append(ri/m)
    file1.write(str(ri/m) + "\n")
    si.append(i)

file1.close()

# Generador de los puntos

x = []
y = []
z = []
ri = r0

for i in range(400):
    ri = (a*ri + c) % m
    x.append(ri/m)
    ri = (a*ri + c) % m
    y.append(ri/m)
    ri = (a*ri + c) % m
    z.append(ri/m)


fig = plt.figure(figsize=plt.figaspect(3.))
fig.suptitle('Números Aleatorios')

ax = fig.add_subplot(1, 3, 1, projection='3d')
ax.scatter(x, y, z, c='red')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax = fig.add_subplot(1, 3, 2)
ax.set_xlabel("i")
ax.set_ylabel("$r_i$")
ax.scatter(si, r, c='blue')
ax.grid()

ax = fig.add_subplot(1, 3, 3)
ax.scatter(x, y, c='green')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid()

plt.show()