import random

import numpy as np


def make(Q):
    shape = np.shape(Q)
    p = np.matrix([[0 for i in range(shape[1])] for j in range(shape[0])])
    for i in range(shape[0]):
        p[i,:] = np.random.rand(1,shape[1]) < np.power(Q[i, :], 2)
    return p
