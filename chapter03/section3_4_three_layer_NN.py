import numpy as np

from chapter03.sectino3_2_activating_function import np_sigmoid


def layer(A, W, b):
    z = np.dot(A, W) + b
    return z


def identity_function(x):
    return x


def middle_layer(A, W, b):
    return np_sigmoid(layer(A, W, b))


def last_layer(A, W, b):
    print(Y)
    return identity_function(layer(A, W, b))


def init_network():
    network = {'1': {}, '2': {}, '3': {}}
    network['1']['W'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['1']['b'] = np.array([0.1, 0.2, 0.3])
    network['2']['W'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['2']['b'] = np.array([0.1, 0.2])
    network['3']['W'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['3']['b'] = np.array([0.1, 0.2])
    return network


def forward(network, x):
    _x = x
    keys = list(network.keys())
    keys.sort()
    for k in keys[:len(keys) - 1]:
        print("Z{}".format(k))
        _x = middle_layer(_x, **network[k])
        print(_x)
    print("Y")
    y = last_layer(_x, **network[str(keys.pop(-1))])
    print(y)
    return y


if __name__ == '__main__':
    X = np.array([1.0, 0.5])
    W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    B1 = np.array([0.1, 0.2, 0.3])
    print("A1 : {}".format(layer(X, W1, B1)))
    Z1 = np_sigmoid(layer(X, W1, B1))
    print("Z1 : {}".format(Z1))

    W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    B2 = np.array([0.1, 0.2])
    print("A2 : {}".format(layer(Z1, W2, B2)))
    Z2 = np_sigmoid(layer(Z1, W2, B2))
    print("Z2 : {}".format(Z2))

    W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
    B3 = np.array([0.1, 0.2])
    print("A3 : {}".format(layer(Z2, W3, B3)))
    Y = identity_function(layer(Z2, W3, B3))
    print(" Y : {}".format(Y))

    network = init_network()
    forward(network, X)
