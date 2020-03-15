import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

# 竖直合并 vertical stack
C = np.vstack((A, B))
print(C)
print(A.shape, " ", C.shape)  # 因为返回是元组，只有单独一个列数，所以需要有逗号防止退化成整数
print("*" * 100)

# 水平合并 horizontal stack
D = np.hstack((A, B))
print(D)
print(A.shape, " ", D.shape)
print("*" * 100)

# 将矩阵反转，首先测试一下转置，证明如果是向量，这并不会改变成 3*1 的矩阵
print(A, A.T, A.T.shape)
print("*" * 100)

# 所以应该使用reshape，并且制定A的size即有几个元素为第一个参数，这样A改变，代码不用重调
E = A.reshape(A.size, 1)
print(A, "\n", E, E.shape)
print("*" * 100)
