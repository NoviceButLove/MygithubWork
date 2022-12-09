import pandas as pd
import numpy as np
df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])

print(df)
print('-------------------------')
'''
lambda定义无名函数，np.sum()返回一个series
同时，df.apply 是创建了一个新的对象
所以打印df还是之前那个
'''
df1 = df.apply(lambda x: np.sum(x), axis=1)
print(df1)
print(type(df1))

print('---------------------')


def cubic(x):
    return x**3


df2 = df.apply(cubic)
print(df2)
print(df2['A'].dtype)  # 返回Series的类型
print('-----------------------------')
file1 = r'C:\Users\86151\Desktop\File_Test\enligh_test.xlsx'
gp = pd.read_excel(file1)
gp = gp.dropna(axis=0, how='any')
print(type(gp['我的练习时长']))
'''
gp0 = gp.dropna(axis=0, how='any')
gp1 = gp0.groupby('授课教师')
#print(type(gp['我的练习时长']))
gp1 = gp1['我的练习完成度'].mean()
#gp1 = gp1.sort_values(ascending=False)
#print(gp1)
'''
print('------------------------------')
dict1 = {'男': 'male', '女': 'female'}
gp['new_gender'] = gp['性别'].map(dict1)  # 值的替换
print(gp.head(3))
print(gp['new_gender'].value_counts())  # 枚举，值的计数
print('---------------------------')
