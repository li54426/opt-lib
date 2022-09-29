import numpy as np


result = np.random.randint(0, 100)
print(result)

index =np.nonzero([0, 1, 2, 3])
print(np.subtract(1,np.matrix([0, 0, 1, 1])))
for i in index:
    print(i)

a = np.matrix([[1, 2], [3, 4]])
b = np.transpose(np.matrix([1, 2]))
result = np.matmul(a, b)
print(result)
er = np.arcsin(-0.5**0.5)
print(er)
a = [1, 2]
b = [[3], [4]]
a = np.array(np.transpose(np.matrix(b))).tolist()
Q = [[[0, 1] for i in range(100)] for j in range(50)]
print(Q)