import numpy as np

a = np.arange(4)
print(a)

# 都是引用
b = a

a[0] = 11
print(a, b)

# 取消关联，深拷贝
c = a.copy()
c[0] = 0
print(a, c)
