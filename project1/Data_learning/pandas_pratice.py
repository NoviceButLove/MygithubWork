import pandas as pd
import numpy as np

obj1 = pd.Series([5, -3, 6, -7], index=['a', 'b', 'c', 'd'])  # Series型数据，一列
print(obj1)
print(obj1.index)
print(obj1[obj1 > 0])  # 利用布尔型数组进行过滤
print(obj1 * 2)  # 进行标量乘法
"""将Series看成定长字典"""

#  搜索字典，判断字典
print('-------------------------------')
if 'b' in obj1:
    print('True')
    print(obj1['b'])
else:
    print('False')
poop = {'Neavada': {2001: 2.5, 2002: 2.8},
        'Ohio': {2000: 1.5, 2001: 1.5, 2002: 3.5}}
"""外层为列索引，内层为行索引"""
frame3 = pd.DataFrame(poop)
print(frame3)
print(frame3.T)  # T 倒转行和列
"""reindex 重新设置index，method参数可用于缺失值的处理"""
obj2 = pd.Series(['blue', 'purple', 'yellow', 'red'], index=[0, 3, 6, 9])
print(obj2)
print('-----------99999999999999999-----------------------')
print(obj2.reindex(range(9), method='ffill'))  # range，第一个参数产生改变量
# method指定用什么方法处理（向前填充
print('---------------------------------------')
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print('---------000000000000---------------')
print(data['one'])  # 可以直接选取列
# print(data['Ohio']  不行
print(data < 5)  # 返回一个布尔型数组,可用于条件查询
print(data[data < 5])  # 结果
print('----------------2022-12-15')
frame2 = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                      columns=list('bde'),
                      index=['Utah', 'Ohio', 'Texas', ' Oregon'])
series1 = frame2.iloc[0]  # 单个Series是一行
"""Series 与 Dataframe 之间进行相加减操作，按行进行"""
j1 = frame2 - series1
print(j1)
print('-----------j0000000000000--------')
"""以上方法可指定轴向"""
series2 = frame2['d']  # series2取了‘d’这一列
print(series2)
j2 = frame2.sub(series2, axis=0)
print(j2)
"""apply默认对列进行操作，可指定axis=0"""
"""一行却是由Series创建"""
