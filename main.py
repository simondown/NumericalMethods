import math
import numpy as np
import matplotlib.pyplot as plt
from formula import *
from solve import *

eps = 1.e-15

print("Введите количество точек приближения:")
N = int(input())

h = 1/(N-1)

u = np.zeros(N)

u[1] = bi(N, eps)

for _ in range(2, N):
    u[_] = 2*(1+h*h)*u[_-1] - u[_-2] - f3(_*h)*h*h

u = np.flip(u)

points = [_*h for _ in range(N)]

fig, axes = plt.subplots()

axes.set_title('n=200')

axes.plot(points, u, 'r')

#plt.show()
plt.savefig('200.jpg')
