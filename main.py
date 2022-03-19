from scipy import random
import numpy as np
import matplotlib.pyplot as plt


def calc_for_draw(a, b, n):
    plt_vals = []
    for i in range(n):
        ar = [0] * n
    for i in range(len(ar)):
        ar[i] = random.uniform(a, b)
    integral = 0.0
    for i in ar:
        integral += function_one(i)
        ans = (b - a) / float(n) * integral
        plt_vals.append(ans)
    return plt_vals


def function_one(x):
    return np.log(np.cos(x) ** 2)


def monte_carlo_of_one_param(a, b, n):
    integral = 0.0
    for i in range(n):
        integral += function_one(random.uniform(a, b))
    return (b - a) / float(n) * integral


def draw(a, b, n):
    plt.title("Distributions of areas calculated")
    plt.hist(calc_for_draw(a, b, n), bins=30, ec="black")
    plt.xlabel("Areas")
    plt.show()


def function_two(x, y):
    return 5


def monte_carlo_of_two_params(a, b, c, d, n):
    integral = 0.0
    for i in range(n):
        integral += function_two(random.uniform(a, b), random.uniform(c, d))
    return (b - a) * (d - c) / float(n) * integral


def method_of_left_rectangles_2_params(a, b, c, d, n):
    integral = 0.0
    h_x = (b - a) / n
    h_y = (d - c) / n
    x = np.arange(a, b, h_x)
    y = np.arange(c, d, h_y)
    for i in range(len(x)):
        for j in range(len(y)):
            integral += (function_two(x[i], y[j]))
    return h_x * h_y * integral


if __name__ == '__main__':
    a = 0
    b = 5

    n = 1500

    c = 0
    d = 5
    # draw(a, b, n)
    # print(monte_carlo_of_one_param(a, b, n))
    print("Monte-carlo: ", monte_carlo_of_two_params(a, b, c, d, n))
    print("Method of left rectangles: ", method_of_left_rectangles_2_params(a, b, c, d, n))
