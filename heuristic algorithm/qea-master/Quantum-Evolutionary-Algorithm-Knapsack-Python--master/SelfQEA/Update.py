import numpy as np

"""
    对于值的更新最重要的是角度，这里的角度是有一个表的
    x       b       f(x)>=f(b)      角度
    0       0         false          0
    0       0         true           0
    0       1         false          0.01π
    0       1         true           0
    1       0         false          -0.01π
    1       0         true           0
    1       1         false          0
    1       1         true           0

"""


def update(Q, Q_all, P, b, fitness, globla_fitness):
    shape = np.shape(P)
    for i in range(shape[0]):
        q = Q[i, :]
        q_all = Q_all[i]
        p = P[i, :]
        j = 0
        m = shape[1]
        while j < m:
            quadrant = 0
            # 计算当前的角度在第几象限
            # angle = np.arcsin(q[0, j])
            if q_all[j][0] > 0 and q_all[j][1] > 0:
                quadrant = 1
            elif q_all[j][0] < 0 and q_all[j][1] > 0:
                quadrant = 2
            elif q_all[j][0] < 0 and q_all[j][0] < 0:
                quadrant = 3
            else:
                quadrant = 4
            # 角度1
            if p[0, j] == 0 and b[0, j] == 0 and fitness[i] < globla_fitness:
                if quadrant == 1 or quadrant == 3:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(0), -np.sin(0)],[np.sin(0), np.cos(0)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # 原本q里面记录的就是β，所以这里也只更新β，需要α的时候在使用α^2 + β^2 = 1 来计算
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
                else:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(-0), -np.sin(-0)], [np.sin(-0), np.cos(-0)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
            # 角度2
            if p[0, j] == 0 and b[0, j] == 0 and fitness[i] >= globla_fitness:
                if quadrant == 1 or quadrant == 3:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(0), -np.sin(0)],[np.sin(0), np.cos(0)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # 原本q里面记录的就是β，所以这里也只更新β，需要α的时候在使用α^2 + β^2 = 1 来计算
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
                else:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(-0), -np.sin(-0)], [np.sin(-0), np.cos(-0)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
            # 角度3
            if p[0, j] == 0 and b[0, j] == 1 and fitness[i] < globla_fitness:
                if quadrant == 1 or quadrant == 3:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(0.01*np.pi), -np.sin(0.01*np.pi)],[np.sin(0.01*np.pi), np.cos(0.01*np.pi)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # 原本q里面记录的就是β，所以这里也只更新β，需要α的时候在使用α^2 + β^2 = 1 来计算
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
                else:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(-0.01*np.pi), -np.sin(-0.01*np.pi)], [np.sin(-0.01*np.pi), np.cos(-0.01*np.pi)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
            # 角度4
            if p[0, j] == 0 and b[0, j] == 1 and fitness[i] >= globla_fitness:
                if quadrant == 1 or quadrant == 3:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(0), -np.sin(0)],[np.sin(0), np.cos(0)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # 原本q里面记录的就是β，所以这里也只更新β，需要α的时候在使用α^2 + β^2 = 1 来计算
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
                else:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(-0), -np.sin(-0)], [np.sin(-0), np.cos(-0)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
            # 角度5
            if p[0, j] == 1 and b[0, j] == 0 and fitness[i] < globla_fitness:
                if quadrant == 1 or quadrant == 3:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(-0.01*np.pi), -np.sin(-0.01*np.pi)],[np.sin(-0.01*np.pi), np.cos(-0.01*np.pi)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # 原本q里面记录的就是β，所以这里也只更新β，需要α的时候在使用α^2 + β^2 = 1 来计算
                    # q_all[j] = np.array(np.transpose(new_probability))
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
                else:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(-(-0.01*np.pi)), -np.sin(-(-0.01*np.pi))], [np.sin(-(-0.01*np.pi)), np.cos(-(-0.01*np.pi))]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
            # 角度6
            if p[0, j] == 1 and b[0, j] == 0 and fitness[i] >= globla_fitness:
                if quadrant == 1 or quadrant == 3:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(0), -np.sin(0)],[np.sin(0), np.cos(0)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # 原本q里面记录的就是β，所以这里也只更新β，需要α的时候在使用α^2 + β^2 = 1 来计算
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
                else:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(-0), -np.sin(-0)], [np.sin(-0), np.cos(-0)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
            # 角度7
            if p[0, j] == 1 and b[0, j] == 1 and fitness[i] < globla_fitness:
                if quadrant == 1 or quadrant == 3:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(0), -np.sin(0)],[np.sin(0), np.cos(0)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # 原本q里面记录的就是β，所以这里也只更新β，需要α的时候在使用α^2 + β^2 = 1 来计算
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
                else:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(-0), -np.sin(-0)], [np.sin(-0), np.cos(-0)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
            # 角度8
            if p[0, j] == 1 and b[0, j] == 1 and fitness[i] >= globla_fitness:
                if quadrant == 1 or quadrant == 3:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(0), -np.sin(0)],[np.sin(0), np.cos(0)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # 原本q里面记录的就是β，所以这里也只更新β，需要α的时候在使用α^2 + β^2 = 1 来计算
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
                else:
                    # 计算新的概率
                    new_probability = np.matmul(np.matrix([[np.cos(-0), -np.sin(-0)], [np.sin(-0), np.cos(-0)]]), np.transpose(np.matrix([(1-np.power(q[0, j],2))**0.5, q[0, j]])))
                    # q_all[j] = new_probability
                    q_all[j] = np.array(np.transpose(new_probability)).tolist()[0]
                    q[0, j] = new_probability[1, 0]
            j = j + 1
        # 更新Q[i]
        Q_all[i] = q_all
        Q[i, :] = q
    return Q, Q_all

