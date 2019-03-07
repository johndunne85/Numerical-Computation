from numpy import dot
import numpy as np


matrix = np.array([[4,-2,1],[-2,4,-2],[1,-2,4]], np.float32)
sols = np.array([11,-16,17], np.float32)



def gaussElimin(a,b):
    n = len(b)

    for k in range(0, n-1):
        for i in range(k+1,n):
            if a[i][k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] = lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]


    for k in range(n-1,-1,-1):
        b[k] = (b[k] - dot(a[k,k+1:n], b[k+1:n]))/a[k,k]
    return b


ans = gaussElimin(matrix, sols)

print(ans)
