import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt


def function(x):
    return x * np.arccos(1 / x)


def integrated_function(x):
    return 1 / 2 * (x ** 2 * np.arccos(1 / x) - np.sqrt(x ** 2 - 1))


def analytical_integral(a, b):
    return integrated_function(b) - integrated_function(a)


def rectangles_integral(a, b, n):  # left rectangles method
    integral = 0
    h = (b - a) / n
    for i in range(n):
        integral += function(a + i * h)
    return integral * h


def trapezoids_integral(a, b, n):
    integral = 0
    h = (b - a) / n
    integral += function(a)
    integral += function(b)
    for i in range(1, n):
        integral += 2 * function(a + i * h)
    return integral * h / 2


def parabolas_integral(a, b, n):
    if n % 2 == 1:
        n += 1
    integral = 0
    h = (b - a) / n
    integral += function(a)
    integral += function(b)
    for i in range(1, n):
        if i % 2 == 1:
            integral += 4 * function(a + i * h)
        else:
            integral += 2 * function(a + i * h)
    return integral * h / 3


def cube_parabolas_integral(a, b, n):
    while n % 3 != 0:
        n += 1
    integral = 0
    h = (b - a) / n
    integral += function(a)
    integral += function(b)
    for i in range(1, n):
        if i % 3 == 0:
            integral += 2 * function(a + i * h)
        else:
            integral += 3 * function(a + i * h)
    return integral * 3 * h / 8


def boole_integral(a, b, n):
    while n % 4 != 0:
        n += 1
    h = (b - a) / n
    integral = 0
    integral += function(a)
    integral += function(b)
    integral *= 7
    for i in range(1, n):
        if i % 2 == 1:
            integral += 32 * function(a + i * h)
        elif i % 4 == 0:
            integral += 14 * function(a + i * h)
        elif i % 2 == 0:
            integral += 12 * function(a + i * h)
    return integral * 2 * h / 45


def draw_function(a, b, n):
    h = (b - a) / n
    x = np.arange(a - h, b + 2 * h, h)
    y = function(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='x', ylabel='y', title='y = x * arccos(1 / x)')
    ax.grid()
    plt.show()


def draw_difference(a, b):
    n = np.arange(1, 100)
    fig, ax = plt.subplots()
    excepted = analytical_integral(a, b)
    r1 = [rectangles_integral(a, b, n) - excepted for n in n]
    ax.plot(n, np.abs(r1), 'b')
    r2 = [trapezoids_integral(a, b, n) - excepted for n in n]
    ax.plot(n, np.abs(r2), 'r')
    r3 = [parabolas_integral(a, b, n) - excepted for n in n]
    ax.plot(n, np.abs(r3), 'g')
    r4 = [cube_parabolas_integral(a, b, n) - excepted for n in n]
    ax.plot(n, np.abs(r4), 'y')
    r5 = [boole_integral(a, b, n) - excepted for n in n]
    ax.plot(n, np.abs(r5), 'c')
    ax.set(xlabel='n', ylabel='eps', title='y = x * arccos(1 / x)')
    ax.grid()
    plt.yscale('log')
    plt.show()


if __name__ == '__main__':
    a = 1
    b = 1.1
    n = 20  # h = 0.2
    to_print = "{0} output: {1}"
    print(to_print.format("Rectangles method", rectangles_integral(a, b, n)))
    print(to_print.format("Trapezoids method", trapezoids_integral(a, b, n)))
    print(to_print.format("Parabolas method", parabolas_integral(a, b, n)))
    print(to_print.format("Cube parabolas method", cube_parabolas_integral(a, b, n)))
    print(to_print.format("Boole's method", boole_integral(a, b, n)))
    print(to_print.format("Scipy", integrate.quad(function, a, b, limit=100)[0]))
    print(to_print.format("Analytical", analytical_integral(a, b)))
    draw_function(a, b, n)
    draw_difference(a, b)
