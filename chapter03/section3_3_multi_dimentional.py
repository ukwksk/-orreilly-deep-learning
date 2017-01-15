import numpy as np


def show_array(array):
    print(array)
    print(np.ndim(array))
    print(array.shape)
    print(array.shape[0])


def NNdot(X, W):
    print(X)
    print(W)
    print("shape: {}, {}".format(X.shape, W.shape))
    print(np.dot(X, W))


if __name__ == '__main__':
    A = np.array([1, 2, 3, 4])
    B = np.array([[1, 2], [3, 4], [5, 6]])
    show_array(A)
    show_array(B)

    C = np.array([[1, 2], [3, 4]])
    D = np.array([[5, 6], [7, 8]])
    print(np.dot(C, D))
    print(np.dot(D, C))

    NNdot(np.array([1, 2]), np.array([[1, 3, 5], [2, 4, 6]]))
