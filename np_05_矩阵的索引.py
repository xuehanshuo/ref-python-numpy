import numpy as np

A = np.arange(3, 15).reshape((3, 4))
print(A)
print("*" * 100)

# 索引某一行/某一列
print(A[2])
print(A[2, :])
print(A[:, 0])
print("*" * 100)

# 索引单个值
print(A[0, 0])
print(A[0][0])
print("*" * 100)

# 索引部分值
print(A[0, 1:3])  # 第0行，[1,3)的所有数
print("*" * 100)

# 迭代每一行
for row in A:
    print(row)
print("*" * 100)

# 迭代每一列
for column in A.T:
    print(column)
print("*" * 100)

# 迭代每一个元素
for item in A.flat:
    print(item)
print(A.flatten())  # 延展出来一行
print("*" * 100)
