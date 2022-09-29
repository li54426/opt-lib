def Knapsack_observe(Q):
    import numpy as np

    s = np.shape(Q)
    t = np.random.rand(1,s[1]) < np.power(np.sin(Q),2) #求概率
    return  t