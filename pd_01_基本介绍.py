import numpy as np
import pandas as pd

# 含有序列的一组数，类似于字典
s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)

# 储存索引
dates = pd.date_range("20200101", periods=6)
print(dates)
print("*" * 100)

# 结合起来
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

# 查看类型，行索引，列索引，值，和各种数字的描述信息
print(df.dtypes)
print(df.index)
print(df.columns)
print(df.values)
print(df.describe())
print("*" * 100)

# 转置
print(df.T)

# 索引排序
print(df.sort_index(axis=1, ascending=False))  # 1行0列，水平的降序
# 值排序
print(df.sort_values(by='a'))
