import numpy as np

"""
    本方法的主要的作用是更新B,也就是个体的历史最佳适应度序列
"""
def update_b(B, P, individual_fitness, fitness):
    shape = np.shape(fitness)
    for i in range(shape[0]):
        # 通过对比B(t - 1)的适应度和P(t)的适应度来决定是不是需要更新B(t)对应的序列
        if (fitness[i] > individual_fitness[i]):
            B[i] = P[i]
    return B