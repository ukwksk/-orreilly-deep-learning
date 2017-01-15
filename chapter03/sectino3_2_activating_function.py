import numpy as np
import matplotlib.pylab as plt


def show_result(func):
    x = np.arange(-5.0, 5.0, 0.1)
    y = func(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()


def step_function(x):
    if x > 0:
        return 1
    else:
        return 0


def np_step_function(x):
    y = x > 0
    return y.astype(np.int)


def np_sigmoid(x):
    return 1 / (1 + np.exp(-x))


def np_relu(x):
    return np.maximum(0, x)


if __name__ == '__main__':
    show_result(np_step_function)
    show_result(np_sigmoid)
    show_result(np_relu)
