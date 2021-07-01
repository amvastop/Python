import matplotlib.pyplot as plt
import numpy as np
import math
l = 25
T = 150
h = 1
dt = h ** 2 / 3.8 
x = int(l / h + 1)
t = int(T / dt + 1)
u = [[10] * x for i in range(t)]
for n in range(0, t-1):
    for j in range(1, x - 1):
        u[n + 1][j] = u[n][j] + (1.8 * dt)/(h ** 2) * (u[n][j + 1] - 2 * u[n][j] + u[n][j - 1]) 
    u[n + 1][0] = 0
    u[n + 1][x - 1] = 20


# for n in range(0, t):
#     plt.plot(range(0, x),u[n])
# plt.show()

# k = []
# for i in [5,10,15,3,20, 21, 18]:
#     for n in range(0, t):
#         k.append(u[n][int(i/h)])
#     plt.plot(range(0, t),k, label = 'u({},t)'.format(i))
#     k.clear()
# plt.legend()
# plt.show()

z = []
for i in range(50, t - 50):
    sum = 0
    for j in range(0, x):
        s = 0
        for n in range(1,6):
            s+= (10 + 20 * (-1) ** n) * math.exp(-math.pi ** 2 * n ** 2 * 1.8 * i / l ** 2) * math.sin(math.pi * n * j / l)
        sum += (u[i][j] - (20 * j / l + 2/math.pi * s)) ** 2
    z.append(math.sqrt(sum))
plt.plot(range(50, t - 50) , z)
plt.show()


