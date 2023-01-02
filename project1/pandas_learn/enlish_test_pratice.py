import pandas as pd
import numpy as np
f1 = pd.read_excel(r'C:\Users\86151\Desktop\File_Test\enligh_test.xlsx')
print(f1.head(3))
# print(f1.describe())
print(f1['姓名'].loc[f1.duplicated()])
gender_dict = {'男': 'male', '女': 'female'}
f1['gender'] = f1['性别'].replace(gender_dict)
print(f1['gender'])
f1.fillna('NA', inplace=True)
print(f1['gender'].value_counts())
print(f1.loc[f1['性别'].isnull()])
"""离散化和面元划分"""
"""cut 函数，按区间划分"""
ages = [3, 13, 33, 42, 26, 63, 34, 23, 54, 12, 32, 16, 16, 18, 19,
        12, 22, 23, 34, 36, 23, 38, 45, 45, 42, 43, 31, 48, 56,
        16, 18, 23, 27, 35, 45, 50, 65, 80, 100]
bins = [3, 12, 18, 30, 50, 65, 80, 100]
print(pd.cut(ages, bins))
"""自己指定label显示分类结果"""
data = np.random.rand(20)
name4 = ['Gold', 'Silvery', 'Brass', 'Wood']
print(pd.cut(data, 4, precision=2, labels=name4))  # 离散切片data，分成5组，小数精确2位

data1 = pd.Series(np.random.randn(9),
                  index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                         [1, 2, 3, 1, 3, 1, 2, 2, 3]])
print(data1)
print('==========================')
# print(data1.unstack())
data1.index.names = ['key1', 'key2']
print(data1)
print('-------------------------')
print(data1.swaplevel('key1', 'key2'))  # swaplevel 交换列名
print(data1.sort_index(level=1))  # 按列名值排序，以1列为准，（即第二层）
print('---------merge的使用方法------------')
lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio',
                               'Nevada', 'Neavada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio',
                             'Ohio', 'Ohio'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])
print(lefth)
print('-------------------0000000000000')
print(righth)
merg1 = pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True,
                 how='outer')
print(merg1)
print('--------------------------')
arr = np.arange(12).reshape((3, 4))
print(arr)
print('=========concatenate===========')
arr1 = np.concatenate([arr, arr], axis=0)
print(arr1)
print('-----------------concat----------------')
s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4, 1], index=['c', 'd', 'e', 'a'])
s3 = pd.Series([5, 6], index=['g', 'h'])
con1 = pd.concat([s1, s2, s3], axis=0)
print(con1)
