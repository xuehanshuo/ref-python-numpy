import numpy as np
import pandas as pd

dates = pd.date_range("20200101", periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)

# 打印某一列
print(df.A, df['A'])
print("*" * 100)

# 打印某一段的行切片
print(df[0:3], "\n", df['20200101':'20200103'])
print("*" * 100)

# select by label:loc
print(df.loc['20200101'])
print(df.loc[:, ['A', 'B']])
print(df.loc["20200101", ['A', 'B']])
print("*" * 100)

# select by position:iloc
print(df.iloc[3])  # 第三行
print(df.iloc[3, 1])  # 第三行，第一位
print(df.iloc[3:5, 1:3])  # 切片：第三行到第五行，第一列到第三列
print(df.iloc[[1, 3, 5], 1:3])  # 不连续的筛选
print("*" * 100)

# Boolean indexing
# 先找出这一列中符合要求的行，之后打印对应行的所有
print(df[df.A > 8])
