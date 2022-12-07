import pandas as pd
import matplotlib as mpl

name = r'C:\Users\86151\Desktop\File_Test\weather\testset.csv'
f1 = pd.read_csv(name)
f1.dropna(axis=0, how='any')
print(f1.head(3))
print(f1.describe())
print(f1.columns)
f1.groupby('datetime_utc')
print(f1.head(3))
print('-----------------------------------')
f2 = f1.groupby([f1['datetime_utc'],f1[' _conds']])
print(f2.head(3))
print('=======================')
