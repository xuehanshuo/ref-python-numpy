import numpy as np

# 将列表转换为矩阵
array = np.array([[1, 2, 3],
                  [2, 3, 4],
                  [3, 4, 5]])

# 打印矩阵
print(array)
print("*" * 100)

# 打印数组的维度
print("number of dim:", array.ndim)
print("*" * 100)

# 是 几*几 的矩阵
print("shape:", array.shape)
print("*" * 100)

# 总共有多少元素
print("size:", array.size)
print("*" * 100)
