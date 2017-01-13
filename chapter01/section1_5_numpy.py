import traceback

import numpy as np

print("==== Examples of 1-dimensional array ====")

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print("x: {}".format(x))
print("y: {}".format(y))

print("type(x): {}".format(type(x)))

print("x+y: {}".format(x + y))
print("x-y: {}".format(x - y))
print("x*y: {}".format(x * y))
print("x/y: {}".format(x / y))

print("x/2: {}".format(x / 2))

# This is called "broadcast"
try:
    a = np.array([1.0])
    print("a: {}".format(a))
    print("x+a {}".format(x + a))
except Exception as e:
    print(traceback.format_exc())

try:
    b = np.array([1.0, 2.0])
    print("b: {}".format(b))
    print("x+b: {}".format(x + b))
except Exception as e:
    print(traceback.format_exc())

print("==== Examples of N-dimensional array ====")

X = np.array([[1, 2], [3, 4]])
print("X: {}".format(X))
print("X.shape: {}".format(X.shape))
print("X.dtype: {}".format(X.dtype))

Y = np.array([[3, 0], [0, 6]])
print("Y: {}".format(Y))
print("X+Y: {}".format(X + Y))
print("X*Y: {}".format(X * Y))

print("X*10: {}".format(X * 10))

# This is called "broadcast"
try:
    A = np.array([[1.0]])
    print("A: {}".format(A))
    print("X+A: {}".format(X + A))
except Exception as e:
    print(traceback.format_exc())

# This is called "broadcast"
try:
    B = np.array([[1.0, 2.0]])
    print("B: {}".format(B))
    print("X+B: {}".format(X + B))
except Exception as e:
    print(traceback.format_exc())

try:
    C = np.array([[1.0, 2.0, 3.0]])
    print("C: {}".format(C))
    print("X+C: {}".format(X + C))
except Exception as e:
    print(traceback.format_exc())

try:
    D = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]])
    print("D: {}".format(D))
    print("X+D: {}".format(X + D))
except Exception as e:
    print(traceback.format_exc())

print("==== Examples of entity access ====")

print("X: {}".format(X))
print("X[0]: {}".format(X[0]))
print("X[0][0]: {}".format(X[0][0]))
for row in X:
    print("outer-loop: {}".format(row))
    for col in row:
        print("inner-loop: {}".format(col))

print("X.flatten(): {}".format(X.flatten()))
print("X.flatten()[np.array([1,3])]: {}".format(X.flatten()[np.array([1, 3])]))
print("X.flatten() % 2 == 0: {}".format(X.flatten() % 2 == 0))
print("X.flatten()[X.flatten() % 2 == 0]: {}".format(X.flatten()[X.flatten() % 2 == 0]))
