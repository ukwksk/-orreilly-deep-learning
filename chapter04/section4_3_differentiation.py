import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def f1(x):
    return 0.01 * x ** 2 + 0.1 * x


def diff1(x, a):
    return numerical_diff(f1, a) * (x - a) + f1(a)


def f2(x):
    # return np.sum(x ** 2)
    return x[0] ** 2 + x[1] ** 2


def f2_tmp0(x0):
    return x0 ** 2 + 4 ** 2


def diff2_1(x):
    return numerical_diff(f2_tmp0, x)


def f2_tmp1(x1):
    return 3 ** 2 + x1 ** 2


def diff2_2(x):
    return numerical_diff(f2_tmp1, x)


if __name__ == '__main__':
    x = np.arange(-20.0, 20.0, 0.1)
    y = f1(x)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x, y)
    d1 = diff1(x, 0)
    plt.plot(x, d1, color="blue", linestyle="--")
    d2 = diff1(x, -10)
    plt.plot(x, d2, color="green", linestyle=":")
    plt.show()

    # http://d.hatena.ne.jp/white_wheels/20100327/p3
    x, y = np.arange(-20.0, 20.0, 1), np.arange(-20.0, 20.0, 1)
    X, Y = np.meshgrid(x, y)
    print(np.meshgrid(x, y))
    print(X)  # 20*20 の x座標の値
    print(Y)  # 20*20 の y座標の値
    Z = f2(np.meshgrid(x, y))
    print(Z)  # 20*20 の z座標の値
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(X, Y, Z)
    plt.show()

    print(diff2_1(3))
    print(diff2_2(4))