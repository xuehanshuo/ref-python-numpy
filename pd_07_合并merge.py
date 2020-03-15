import pandas as pd

# merge
# 一列key
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)
print("*" * 100)

# 按照哪一栏合并
print(pd.merge(left, right, on='key'))

# 两列的key
left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
print(left1)
print(right1)

# how = ['left','right','outer','inner']
# indicator 显示合并方式
print(pd.merge(left1, right1, on=['key1', 'key2'], how='outer', indicator='indicator_column'))  # 添加名字

# 根据索引合并
left2 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']},
                     index=['K0', 'K1', 'K2', 'K3'])
right2 = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']},
                      index=['K0', 'K1', 'K2', 'K3'])
print(pd.merge(left, right, left_index=True, right_index=True, how='outer'))
print("*" * 100)

# suffixes
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'],
                     'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'],
                      'age': [4, 5, 6]})

print(boys)
print(girls)

print(pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='outer'))
