import numpy as np


def fitness_computer(P, profit):
    shape = np.shape(P)
    fitness = [0 for i in range(shape[0])]
    for i in range(shape[0]):
        fitness[i] = np.sum(np.multiply(P[i], profit))
    return fitness