import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(a, b)
print("*" * 100)

print(a - b)
print(a + b)
print("*" * 100)

# 将a中所有元素进行平方
print(a ** 2)
print("*" * 100)
# 对a中每个元素求sin再都乘以10，使用弧度制
print(10 * np.sin(a))
print("*" * 100)

# 数组的逻辑运算
print(b < 3)
print("*" * 100)

c = np.array([[1, 2],
              [3, 4]])
d = np.arange(4).reshape(2, 2)

# 对应相乘和矩阵相乘
print(c * d)  # 对应
print(np.dot(c, d))  # 矩阵
print(c.dot(d))
print("*" * 100)

# 生成随机几行几列的矩阵, 值处于0和1之间
# 第一个random是模块，第二个是函数
e = np.random.random((2, 4))
print(e)
print("*" * 100)

# 求和 求最小值和最大值
print(np.sum(e), np.max(e), np.min(e))
print("*" * 100)

# 1行0列 求每一行/列的 sum，max，min 返回矩阵
print(np.sum(e, axis=1))
print(np.max(e, axis=0))
print(np.min(e, axis=0))
print("*" * 100)
