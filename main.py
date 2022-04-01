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


def function_log(x):
    return np.log(3 + x ** 2)


def rectangles_integral(a, b, n):  # left rectangles method
    integral_pow = 0
    integral_log = 0
    h = (b - a) / n
    for i in range(n):
        integral_pow += function_pow(a + i * h)
        integral_log += function_log(a + i * h)
    return integral_pow * h, integral_log * h


def trapezoids_integral(a, b, n):
    integral_pow = 0
    integral_log = 0
    h = (b - a) / n
    integral_pow += function_pow(a)
    integral_pow += function_pow(b)
    integral_log += function_log(a)
    integral_log += function_log(b)
    for i in range(1, n):
        integral_pow += 2 * function_pow(a + i * h)
        integral_log += 2 * function_log(a + i * h)
    return integral_pow * h / 2, integral_log * h / 2


def parabolas_integral(a, b, n):
    if n % 2 == 1:
        n += 1
    integral_pow = 0
    integral_log = 0
    h = (b - a) / n
    integral_pow += function_pow(a)
    integral_pow += function_pow(b)
    integral_log += function_log(b)
    integral_log += function_log(b)
    for i in range(1, n):
        if i % 2 == 1:
            integral_pow += 4 * function_pow(a + i * h)
            integral_log += 4 * function_log(a + i * h)
        else:
            integral_pow += 2 * function_pow(a + i * h)
            integral_log += 2 * function_log(a + i * h)
    return integral_pow * h / 3, integral_log * h / 3


def cube_parabolas_integral(a, b, n):
    while n % 3 != 0:
        n += 1
    integral_pow = 0
    integral_log = 0
    h = (b - a) / n
    integral_pow += function_pow(a)
    integral_pow += function_pow(b)
    integral_log += function_log(b)
    integral_log += function_log(b)
    for i in range(1, n):
        if i % 3 == 0:
            integral_pow += 2 * function_pow(a + i * h)
            integral_log += 2 * function_log(a + i * h)
        else:
            integral_pow += 3 * function_pow(a + i * h)
            integral_log += 3 * function_log(a + i * h)
    return integral_pow * 3 * h / 8, integral_log * 3 * h / 8


def boole_integral(a, b, n):
    while n % 4 != 0:
        n += 1
    h = (b - a) / n
    integral_pow = 0
    integral_log = 0
    integral_pow += function_pow(a)
    integral_pow += function_pow(b)
    integral_pow *= 7
    integral_log += function_log(a)
    integral_log += function_log(b)
    integral_log *= 7
    for i in range(1, n):
        if i % 2 == 1:
            integral_pow += 32 * function_pow(a + i * h)
            integral_log += 32 * function_log(a + i * h)
        elif i % 4 == 0:
            integral_pow += 14 * function_pow(a + i * h)
            integral_log += 14 * function_log(a + i * h)
        elif i % 2 == 0:
            integral_pow += 12 * function_pow(a + i * h)
            integral_log += 12 * function_log(a + i * h)
    return integral_pow * 2 * h / 45, integral_log * 2 * h / 45


def integral_gauss(a, b, nodes_count):
    answer_pow = 0
    answer_log = 0
    for i in range(nodes_count):
        ksi_i = (b + a) / 2 + (b - a) * x[nodes_count - 1][i] / 2
        answer_pow += c[nodes_count - 1][i] * function_pow(ksi_i)
        answer_log += c[nodes_count - 1][i] * function_log(ksi_i)
    answer_pow *= (b - a) / 2
    answer_log *= (b - a) / 2
    return answer_pow, answer_log


if __name__ == '__main__':
    answers_gauss = integral_gauss(0, 5, 6)
    answers_rec = rectangles_integral(0, 5, 6)
    answers_trap = trapezoids_integral(0, 5, 6)
    answers_parabolas = parabolas_integral(0, 5, 6)
    answers_cube_parabolas = cube_parabolas_integral(0, 5, 6)
    answers_boole = boole_integral(0, 5, 6)
    print("Gauss integral function_pow = {0}, Gauss integral function_log = {1}".format(answers_gauss[0], answers_gauss[1]))
    print("Scipy gauss integral function_pow = {0}, Scipy gauss integral function_log = {1}"
          .format(sp.quadrature(function_pow, 0, 5)[0], sp.quadrature(function_log, 0, 5)[0]))
    print("Rectangle integral function_pow = {0}, Rectangle integral function_log = {1}"
          .format(answers_rec[0], answers_rec[1]))
    print("Trapezoids integral function_pow = {0}, Trapezoids integral function_log = {1}"
          .format(answers_trap[0], answers_trap[1]))
    print("Parabolas integral function_pow = {0}, Parabolas integral function_log = {1}"
          .format(answers_parabolas[0], answers_parabolas[1]))
    print("Cube parabolas integral function_pow = {0}, Cube parabolas integral function_log = {1}"
          .format(answers_cube_parabolas[0], answers_cube_parabolas[1]))
    print("Boole integral function_pow = {0}, Boole integral function_log = {1}"
          .format(answers_boole[0], answers_boole[1]))



