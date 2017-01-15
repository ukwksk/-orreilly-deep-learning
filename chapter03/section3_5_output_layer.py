import numpy as np


def _soft_max(a):
    exp_a = np.exp(a)
    sum_exp = np.sum(exp_a)
    y = exp_a / sum_exp
    print(a, exp_a, sum_exp, y)
    return y


def soft_max(a):
    c = np.max(a)
    exp_a = np.exp(a - c)  # overflow対策
    sum_exp = np.sum(exp_a)
    y = exp_a / sum_exp
    # print(a, exp_a, sum_exp, y)
    return y


if __name__ == '__main__':
    print(soft_max(np.array([0.3, 2.9, 4.0])))
    print(soft_max(np.array([1010, 1000, 990])))  # 対策しないとoverflowを起こす
