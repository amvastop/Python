import matplotlib.pyplot as plt
import numpy as np
import math
V = 4.0
L0 = 10.0
L = 100.0
Tmax =  L/V
h = 0.005
dt = 0.01
Nx = int((L+1) / h)
Nt = int((Tmax+1) / dt)
u = [[0 ] * Nx for j in range(Nt)]
for j in range (0,int((L0+1) / h)):
    u[0][j] = (math.sin(2.0 * math.pi * j * h / L0)) ** 2
r = (V*dt)/(2*h)
for n in range(0,Nt-1):
    for j in range (1, Nx - 1):
        u[n+1][j] = (u[n][j]+ r * (u[n+1][j-1] - u[n][j+1]+ u[n][j]))/(1.0+r)
    u[n+1][Nx-1] = (u[n][Nx-1] + r * (u[n+1][Nx-2] + u[n][Nx-2] - u[n][Nx-1]))/(1.0 +r)

plt.figure ("Z схема")
for n in range(0, Nt, 500):
    plt.plot(np.arange(0, L+1, h),u[n] , label = 'u({},x)'.format(n))
plt.legend()
plt.grid()
plt.show()
#явная разностная схема
# for n in range(0,Nt - 1):
#     for j in range (1, Nx) :
#         u[n+1][j] = u[n][j] - V* dt / h * (u[n][j]-u[n][j-1])
        
# plt.figure ("Явная схема")
# for n in range(Nt-2, Nt):
#     plt.plot(np.arange(0, L+1, h),u[n] , label = 'u({},x)'.format(n))
# plt.legend()
# plt.grid()

# A =  [[0.0 for i in range(Nx)] for j in range(Nt)]

# for n in range(0,Nt):
#     for j in range (0, Nx):
#         A[n][j] = math.sin(2.0 * math.pi*(4 * dt * n - j*h)/L0)**2

# plt.figure ("Аналитическоре решение")
# for n in range(Nt-2, Nt):
#     plt.plot(np.arange(0, L+1, h),A[n] , label = 'A({},x)'.format(n))
# plt.legend()
# plt.grid()

# plt.show()


