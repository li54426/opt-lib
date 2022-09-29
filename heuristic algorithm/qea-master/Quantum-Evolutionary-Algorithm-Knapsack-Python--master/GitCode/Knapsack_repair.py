def Knapsack_repair(x,p,w,C,type):
    import numpy as np
    #---------------------
    def not_func(arr):
        return np.abs(np.subtract(arr, 1))  # 这里其实就是拿到那些未被选择到的商品
    #----------------------

    s = np.shape(x)
    if type ==1:
        while np.sum(np.multiply(w,x)) > C:
            I = np.floor(s[1]*np.random.rand())
            x[0,int(I)] = 0
    if type == 2:
        while np.sum(np.multiply(w,x)) > C: # np.sum(np.multiply(w,x))表示的是求取当前分配方案所产生的重量之和，如果这个重量的累计和已经大于背包的容量
            temp = np.multiply(np.divide(w,p),x) # 计算按照当前所选着的商品，每件商品的单位价值
            mx_pos = np.argmax(temp) # 拿到当前所选择的商品中单位价值最小的商品
            x[0,mx_pos] = 0 # 丢弃掉单位价值最小的商品
        while np.sum(np.multiply(w,x)) <= C:
            temp = np.multiply(np.divide(w,p),not_func(x))  # 拿到当前未被选择的商品的单体价值
            mx_pos = np.argmax(temp)    # 拿出单体价值最小的商品
            x[0,mx_pos] = 1             # 将单体价值最小的商品放入到背包
        x[0,mx_pos] = 0  # 一旦超出了背包的容量就将最后一个加入的商品给丢掉，因为它是最没有价值的
    return  x


