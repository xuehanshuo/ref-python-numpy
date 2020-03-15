import numpy as np
import pandas as pd

# concatenating
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

print(df1)
print(df2)
print(df3)

res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)
print("*" * 100)

# join, ['inner','outer']
# 出现重复索引
df4 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df5 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
print(df4)
print(df5)
# 列并集
res1 = pd.concat([df4, df5], join='outer', ignore_index=True)
print(res1)
# 列交集
res2 = pd.concat([df4, df5], join='inner', ignore_index=True)
print(res2)
print("*" * 100)

# append
print(df1.append([df2, df3], ignore_index=True))
print(df1.append(pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), ignore_index=True))
