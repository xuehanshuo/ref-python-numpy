import numpy as np
import pandas as pd

dates = pd.date_range("20200101", periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)

# 根据索引改变特定位置的值
df.iloc[2, 2] = 111
print(df)

# 根据标签改变特定位置的值
df.loc['20200101', 'A'] = 233
print(df)

# 根据条件筛选，改变一个区域的值
df[df.A > 4] = 0  # A列中大于4的行被选中，对应df的这些行，所有值都变成了0
df.A[df.A > 4] = 0  # 只改变A的这些符合条件的位置
print(df)

# 新增一行
df['F'] = np.nan  # 不设置值
df['G'] = np.arange(1, 7)

print(df)
