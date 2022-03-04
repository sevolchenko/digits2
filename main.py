from scipy import random
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = np.pi
N = 7000


def f(x):
    return np.sin(x)


def calc_for_draw():
    plt_vals = []
    for i in range(N):
        ar = [0] * N
        # for i in range(len(ar)):
        #     ar[i] = random.uniform(a, b)
        ar = np.array([random.random() for i in range(N)])
        integral = 0.0
        for i in ar:
            integral += function(i)
        ans = (b - a) / float(N) * integral
        plt_vals.append(ans)
    return plt_vals


def calc_for_print(arr):
    integral = 0.0
    for i in range(len(arr)):
        integral += function(arr[i])
    return (b - a) / float(N) * integral


def draw():
    plt.title("Distributions of areas calculated")
    plt.hist(calc_for_draw(), bins=30, ec="black")
    plt.xlabel("Areas")
    plt.show()


def function(x):
    return np.log(np.cos(x) ** 2)


if __name__ == '__main__':
    #draw()
    ar = [0] * N
    for i in range(len(ar)):
        ar[i] = random.uniform(a, b)
    print(calc_for_print(ar))


