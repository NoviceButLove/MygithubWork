import pandas as pd
import numpy as np


sl = pd.Series([1, 2, 3,'a', 2.3, 'b'],index=['a', 'b', 'c', 'd', 'e', 'f'])
#指定index 多一个少一个都不行


print(sl)
print('--------------------------------')
print(sl.index)
print('--------------------')
print(sl['b'])
print('--------------------')
print(sl[['a','b','c']])
print('--------------------------')
data = {
    'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
    'year':[2000,2001,2004,2006,2005],
    'pop':[1.4,1.8,3.6,2.4,2.6]
}
df = pd.DataFrame(data)
print(df)
print('--------------------')
print(df.dtypes)
print('---------------')
print(df.columns)
print('--------------------')
print(df.index)





