import numpy as np
import pandas as pd

dates = pd.date_range("20200101", periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=["A", 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)

# 按行/列丢掉有流失数据的行/列
print(df.dropna(axis=0, how='any'))  # how={'any','all'}

# 填充有丢失数据的位置
print(df.fillna(value=0))

# 检查是否有缺失
print(df.isnull())  # 返回矩阵
print(np.any(df.isnull()))  # 只要有一个丢失，就返回True
