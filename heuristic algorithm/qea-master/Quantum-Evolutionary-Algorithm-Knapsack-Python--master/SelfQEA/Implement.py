import numpy as np
import matplotlib.pyplot as plt
from Make import make
from Repair import repair
from Fitness import fitness_computer
from Update import update
from UpdateB import update_b
# 初始化文件的路径
path = "G:\pycharmWorkSpace\Quantum-Evolutionary-Algorithm-Knapsack-Python--master\\100.txt"
# 加载文件
iterm = np.loadtxt(path,dtype=int, delimiter=(" "), unpack=True)
# 取出背包的容量
capacity = iterm[0][0]
# 构建重量和价值的组合[[重量，价值],[重量，价值],[重量，价值].....]
tmp = iterm.transpose()
# 将第一个背包的容量给丢弃
weight_and_profit = np.delete(tmp, (0), axis=0)
# 拿到重量
weight = np.matrix(weight_and_profit[:, 0])
# 拿到价值
profit = np.matrix(weight_and_profit[:, 1])
# q比特的数量
q_size = weight.shape[1]
# 种群的大小
q_population = 50
Q_all = [[[np.sqrt(0.5), np.sqrt(0.5)] for i in range(q_size)] for j in range(q_population)]
# 构建Q种群,这个是单体β
Q = [[np.sqrt(0.5) for i in range(q_size)] for j in range(q_population)]
Q = np.matrix(Q)
# 个体最佳适应度序列
B = np.matrix([[0 for i in range(q_size)] for j in range(q_population)])
# 全局最佳适应度序列
global_b = np.matrix([0 for i in range(q_size)])
# 全局最佳适应度的值
global_fitness = 0
# 当前个体最佳适应度的值
individual_fitness = [0 for i in range(q_population)]
# 迭代次数
iterate = 100
# 当前的代数
t = 0
# 开始观测，其实就是初始化所选择的物品
P = make(Q)
# 处理背包的容量
P = repair(P, weight, capacity)
# 计算当前的适应度
fitness = fitness_computer(P, profit)
# 拿到当前最佳适应度的索引
best_fitness_index = np.argmax(fitness)
# 将当前个体最佳适应度的序列存储到B
B = P
# 记录全局最佳适应度的序列
global_b = P[best_fitness_index]
# 记录全局最佳适应度的值
global_fitness = fitness[best_fitness_index]
# 存储具体的值，用于之后的对比
individual_fitness = fitness
# 历史适应度，用于记录变化的曲线
history_fitness = [0 for i in range(iterate+1)]
history_fitness[0] = global_fitness
while t < iterate:
    t = t + 1
    # 开始观测，其实就是初始化所选择的物品
    P = make(Q)
    # 处理背包的容量
    P = repair(P, weight, capacity)
    # 计算当前的适应度
    fitness = fitness_computer(P, profit)
    # 更新q-bit
    Q, Q_all = update(Q, Q_all, P, global_b, fitness, global_fitness)
    # 更新B
    B = update_b(B, P, individual_fitness, fitness)
    # 判断是否需要更新全局的最佳适应度
    if (global_fitness < np.max(fitness)):
        best_fitness_index = np.argmax(fitness)
        global_fitness = fitness[best_fitness_index]
        global_b = P[best_fitness_index]
    history_fitness[t] = np.max(fitness)



print("最大的价值是：", global_fitness)
print("最大价值商品的选择的方法：", global_b)
print("验证的最大的价值：", np.sum(np.multiply(global_b, profit)))
print("验证的总量之和：", np.sum(np.multiply(global_b, weight)))
plt.plot(range(iterate+1), history_fitness)
plt.show()




