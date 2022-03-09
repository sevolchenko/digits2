from scipy import random
from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt

a = -np.pi
b = np.pi/2

N = 100000

c = 0
d = 1


def calc_for_draw():
    plt_vals = []
    for i in range(N):
        ar = [0] * N
        for i in range(len(ar)):
            ar[i] = random.uniform(a, b)
        integral = 0.0
        for i in ar:
            integral += function(i)
        ans = (b - a) / float(N) * integral
        plt_vals.append(ans)
    return plt_vals


def function_one(x):
    return np.log(np.cos(x) ** 2)


def calc_func_of_one_param():
    integral = 0.0
    for i in range(N):
        integral += function_one(random.uniform(a, b))
    return (b - a) / float(N) * integral


def draw():
    plt.title("Distributions of areas calculated")
    plt.hist(calc_for_draw(), bins=30, ec="black")
    plt.xlabel("Areas")
    plt.show()


def function_two(x, y):
    return 2 * x * np.sin(y)


def calc_func_of_two_params():
    integral = 0.0
    for i in range(N):
        integral += function_two(random.uniform(a, b), random.uniform(c, d))
    return (b - a) * (d - c) / float(N) * integral


if __name__ == '__main__':
    #draw()
    print(calc_func_of_one_param())
    print(calc_func_of_two_params())


