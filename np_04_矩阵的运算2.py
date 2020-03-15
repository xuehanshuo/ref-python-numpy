import numpy as np

A = np.arange(2, 14).reshape(3, 4)
print(A)
print("*" * 100)

# 求最小值和最大值的索引
print(np.argmin(A))
print(np.argmax(A))
print("*" * 100)

# 求平均值
print(np.mean(A), " ", A.mean())
print(np.average(A))
print("*" * 100)

# 求中位数
print(np.median(A))
print("*" * 100)

# 逐步加和
print(np.cumsum(A))
print("*" * 100)

# 求相邻的差
print(np.diff(A))
print("*" * 100)

# 求不是0的值的索引，左边是行索引，右边是列索引
print(np.nonzero(A))
print("*" * 100)

# 排序, 逐行排序
B = np.arange(14, 2, -1).reshape(3, 4)
print(B, "\n", np.sort(B))
print("*" * 100)

# 转置
print(np.transpose(B).dot(B), "\n", B.T)
print("*" * 100)

# clip功能 所有小于5的全部变成5，所有大于9的全部变成9
print(np.clip(B, 5, 9))
print("*" * 100)

# 对列和行求平均值
print(np.mean(B, axis=1))  # 1行
print(np.mean(B, axis=0))  # 0列
print("*" * 100)
