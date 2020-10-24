# **** Arrays ****

import numpy

def arrays(arr):
    return (numpy.array(arr[::-1], float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# **** Shape and Reshape ****

import numpy as np

print(np.array(input().split(), int).reshape(3, 3))

# **** Transpose and Flatten ****

import numpy as np

n, m = map(int, input().split())
array = np.array([input().strip().split() for _ in range(n)], int)
print(array.transpose())
print(array.flatten())

# Concatenate

import numpy as np

a, b, c = map(int, input().split())
A = np.array([input().split() for _ in range(a)], int)
B = np.array([input().split() for _ in range(b)], int)
print(np.concatenate((A, B), axis=0))

# **** Zeros and Ones ****

import numpy

nums = tuple(map(int, input().split()))
print(numpy.zeros(nums, dtype=numpy.int))
print(numpy.ones(nums, dtype=numpy.int))

# **** Eye and Identity ****

import numpy

numpy.set_printoptions(sign=' ')
print(numpy.eye(*map(int, input().split())))

# **** Array Mathematics ****

import numpy as np

n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a + b, a - b, a * b, a // b, a % b, a ** b, sep='\n')

# **** Floor, Ceil and Rint ****

import numpy as np

np.set_printoptions(sign=' ')

a = np.array(input().split(), float)
print(*(f(a) for f in [np.floor, np.ceil, np.rint]), sep='\n')

# **** Sum and Prod ****

import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))

# **** Min and Max ****

import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.max(numpy.min(A, axis=1), axis=0))

# **** Mean, Var, and Std ****

import numpy as np

np.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
array = np.array([input().split() for _ in range(n)], int)
print(np.mean(array, axis=1), np.var(array, axis=0), np.std(array), sep = '\n')

# **** Dot and Cross **** 

import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))

# **** Inner and Outer ****

import numpy as np

A = np.array(input().split(), int)
B = np.array(input().split(), int)
print(np.inner(A, B), np.outer(A, B), sep='\n')

# **** Polynomials ****

import numpy as np

poly = [float(x) for x in input().split()]
x = float(input())
print(np.polyval(poly, x))

# **** Linear Algebra ****

import numpy as np

np.set_printoptions(legacy='1.13')

n = int(input())
array = np.array([input().split() for _ in range(n)], float)
print(np.linalg.det(array))

