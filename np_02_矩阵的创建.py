import numpy as np

# dtype是存储的数据类型
a = np.array([1, 2, 3], dtype=np.int64)  # float64
print(a.dtype)
print("*" * 100)

# 生成一个 几行几列 的 零矩阵
b = np.zeros((3, 2))
print(b)
print("*" * 100)

# 生成一个 几行几列 的 全是几的矩阵
c = 2 * np.ones((3, 4), dtype=np.int16)
print(c)
print("*" * 100)

# 生成一个空矩阵 (内容随机，未初始化)
d = np.empty((3, 4))
print(d)
print("*" * 100)

# 生成单位矩阵
e = np.eye(5)
print(e)
print("*" * 100)

# 生成一个有序的数列 (左闭右开，步长)
f = np.arange(10, 20, 2)
print(f)
print("*" * 100)

# 生成一个指定几行几列的有序数列
g = np.arange(12).reshape(3, 4)
print(g)
print("*" * 100)

# 生成一个指定几段的线性数列 (1开头，10结尾，共6个结点)
h = np.linspace(1, 10, 6).reshape(2, 3)
print(h)
print("*" * 100)