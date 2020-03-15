import numpy as np

A = np.arange(12).reshape(3, 4)
print(A)

# 对每一行进行分割，相当于分成几列
print(np.split(A, 2, axis=1))

print(np.vsplit(A, 3))
print(np.hsplit(A, 2))
