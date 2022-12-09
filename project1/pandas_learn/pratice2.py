from pandas import *
from numpy import *

data = DataFrame(np.arange(16).reshape(4, 4),
                 index=list('ABCD'),
                 columns=list('abcd'))
print(data)
print('---===========-----------')
print(data.loc['A'])  # 注意区别，此处一个一个输出，返回Series
print('--------------------------')
print(data.loc[['A']])  # 此处输出一行，返回Dataframe
print('-------------------------------')
print(data.loc[['B'], ['b']])  # 这种格式，输出行列确定的一个值
print('==------------=================------')
print(data.loc[:, 'a'])  # 这种格式，输出a列所有行
print('--------------------------')
data1 = data['a'].agg(['max', 'min', 'mean'])  # agg后面要加函数来用
print(data1)
