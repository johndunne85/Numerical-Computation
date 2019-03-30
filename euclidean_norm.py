from numpy import linalg as LA
import numpy as np

a = np.arange(9) - 4
print(a)

b = a.reshape((3,3))
print(b)

c = LA.norm(b)

print(c)
