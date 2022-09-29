import random

import numpy as np


# 拿到当前已经选择的商品
def get_chosen_item(item):
   chosen_index = np.nonzero(item)
   return chosen_index[1]


# 拿到当前已经选择的商品
def get_not_selected_item(item):
   not_chosen_index = np.nonzero(np.subtract(1,item))
   return not_chosen_index[1]


# 计算出当前背包的总的总量
def get_gross_weight(items, weight):
    gross_weight = np.sum(np.multiply(items, weight))
    return gross_weight


def repair(P, weight, capacity):
    global not_selected_item
    shape = np.shape(P)
    for i in range(shape[0]):
        # 计算当前所选择的物品的重量，与背包的容量进行对比，如果当前选择得物品的总量是大于背包的容量，我，们就随机的选取一件已经选择的物品丢掉
        chooseItem = P[i, :]
        while get_gross_weight(chooseItem, weight) > capacity:
            # 随机的丢弃一个物品
            chosen = get_chosen_item(chooseItem)
            chooseItem[0, random.choice(chosen)] = 0
        while get_gross_weight(chooseItem, weight) <= capacity:
            # 随机的选择一件未被选择的物品放入背包
            not_selected = get_not_selected_item(chooseItem)
            # 记录当前要加入的物品，等到背包满的时候就可以丢弃最后一个加入的物品
            not_selected_item = random.choice(not_selected)
            chooseItem[0, not_selected_item] = 1
        # 当到这里的时候背包一定是溢出了，我们就直接丢掉最后一次选择的物品
        chooseItem[0, not_selected_item] = 0
        P[i, :] = chooseItem
    return P # 这里返回的其实就是一个个的bi