import math
import numpy as np
from formula import *

def bi(N, eps):

    h = 1/(N-1)

    lb = -1
    rb = 1
    m = 0

    while np.sign(sh(lb, N)) == np.sign(sh(rb,N)):
        lb -= 0.5
        rb += 0.5

    while rb-lb > eps:
        shift = (rb-lb)/2
        m = lb + shift

        if np.sign(sh(lb, N)) == np.sign(sh(m, N)):
            lb = m
        else:
            rb = m

#    print(m)
    return m

def sh(g, N):

    h = 1/(N-1)

    u = np.zeros(N)
    u[1] = g

    i = u[1] + u[1]**3

    for _ in range(2, N):

        u[_] = 2*(1+h*h)*u[_-1] - u[_-2] - f3(_*h)*h*h
        i += (u[_] + u[_]**3)*h

    eps = 1 - i

    return eps

