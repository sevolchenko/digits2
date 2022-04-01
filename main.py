import copy
import numpy as np
import scipy.integrate as sp

x = [[0],
     [-0.5773503, 0.5773503],
     [-0.7745967, 0, 0.7745967],
     [-0.8611363, -0.3399810, 0.3399810, 0.8611363],
     [-0.9061798, -0.5384693, 0, 0.5384693, 0.9061798],
     [-0.9324700, -0.6612094, -0.2386142, 0.2386142, 0.6612094, 0.9324700]]

c = [[2],
     [1, 1],
     [0.5555556, 0.8888889, 0.5555556],
     [0.3478548, 0.6521451, 0.6521451, 0.3478548],
     [0.4786287, 0.2369269, 0.5688888, 0.2369269, 0.4786287],
     [0.1713245, 0.3607616, 0.4679140, 0.4679140, 0.3607616, 0.1713245]]


def function_pow(x):
    return (x + 3) ** 2


def function_log_cos(x):
    return np.log(3 + x ** 2)


def integral_gauss(a, b, nodes_count):
    answer_pow = 0
    answer_log = 0
    for i in range(nodes_count):
        ksi_i = (b + a) / 2 + (b - a) * x[nodes_count - 1][i] / 2
        answer_pow += c[nodes_count - 1][i] * function_pow(ksi_i)
        answer_log += c[nodes_count - 1][i] * function_log_cos(ksi_i)
    answer_pow *= (b - a) / 2
    answer_log *= (b - a) / 2
    return answer_pow, answer_log


if __name__ == '__main__':
    print(function_pow(2))
    answers = integral_gauss(0, 5, 6)
    print("Gauss integral function_pow = {0}, Gauss integral function_log = {1}".format(answers[0], answers[1]))
    print("Scipy gauss integral function_pow = {0}, Scipy gauss integral function_log = {1}"
          .format(sp.quadrature(function_pow, 0, 5)[0], sp.quadrature(function_log_cos, 0, 5)[0]))