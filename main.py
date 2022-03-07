from scipy import random
import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 0

N = 7000

c = 1
d = -3


def f(x):
    return np.sin(x)


def calc_for_draw():
    plt_vals = []
    for i in range(N):
        # ar = [0] * N
        # for i in range(len(ar)):
        #     ar[i] = random.uniform(a, b)
        ar = np.array([random.random() for i in range(N)])
        integral = 0.0
        for i in ar:
            integral += function(i)
        ans = (b - a) / float(N) * integral
        plt_vals.append(ans)
    return plt_vals


def calc_for_print():
    integral = 0.0
    for i in range(N):
        integral += function_one(random.uniform(a, b))
    return (b - a) / float(N) * integral


def draw():
    plt.title("Distributions of areas calculated")
    plt.hist(calc_for_draw(), bins=30, ec="black")
    plt.xlabel("Areas")
    plt.show()


def function_one(x):
    return np.log(np.cos(x) ** 2)


def function_two(x, y):
    return 2 * x * np.sin(y)


def calc_func_of_two_params():
    integral = 0.0
    for i in range(N):
        integral += function_two(random.uniform(a, b), random.uniform(c, d))
    return (b - a) * (d - c) / float(N) * integral


if __name__ == '__main__':
    #draw()
    print(calc_for_print())
    print(calc_func_of_two_params())


