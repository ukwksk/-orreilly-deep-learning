import numpy as np

from chapter02.section2_3_perceptron import np_nand, np_or, np_and, show_result


def np_xor(x1, x2):
    s1 = np_nand(x1, x2)
    s2 = np_or(x1, x2)
    return np_and(s1, s2)


if __name__ == '__main__':
    show_result(np_xor)
