import pandas as pd #导入
import numpy as np

# s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
# print(s)
# print(s.index)
# Reading a csv into Pandas.
df = pd.read_csv('./shs.csv')
print(df.head(5))
print(df.columns)
print(len(df))
print("提取一列数据")
print(df['src'])
