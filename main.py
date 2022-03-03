import numpy as np


def function(x):
    return np.log(np.cos(x) ** 2)


if __name__ == '__main__':
    print(function(2))
