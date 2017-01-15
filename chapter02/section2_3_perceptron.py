import numpy as np


def show_result(func):
    inset = [[0, 0], [1, 0], [0, 1], [1, 1]]
    for i in inset:
        print("{}({}, {}): {}".format(func.__name__, i[0], i[1], func(i[0], i[1])))


def _and(x1, x2):
    w1, w2, theta = 1.0, 1.0, 1.0
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1


def np_and(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1.0, 1.0])
    b = -1.5
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def np_nand(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-1.0, -1.0])
    b = 1.5
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def np_or(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1.0, 1.0])
    b = -0.5
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    show_result(_and)
    show_result(np_and)
    show_result(np_nand)
    show_result(np_or)
