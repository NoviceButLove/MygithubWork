import pandas as pd


file = r'C:\Users\86151\Desktop\File_Test\stock\fundamentals.csv'
f1 = pd.read_csv(file)
print(f1.head(3))
print(f1.columns)
print('-------------------------')
print(f1['Ticker Symbol'].unique())
print('---------1111111111111111111---------------')
f1 = f1.sort_index()
#   用Ticker Symbol来分类，取Earning Before Tax的max
print(f1.groupby('Ticker Symbol')['Earnings Before Tax'].max())
# f2 = f1.unstack()
print('-----------查看税前利润------------------')
# print(f2)
# print(f2.plot())
print(f1['Earnings Before Tax'].dtypes)
print(f1.loc[:, 'Earnings Before Tax'])
print('---------------------')
dict1 = {'AAL': 'aal', 'AAP': 'aap', 'AAPL': 'aapl', 'ABBV': 'abbv'}
f1['new_name'] = f1.iloc[0:16].apply(lambda x: dict1[x['Ticker Symbol']], axis=1)
print(f1.head(16))
print('--------按时期，股票代号分组，查看总现金最大值---------------')
f2 = f1.groupby(['Period Ending',
                'Ticker Symbol'])['Total Current Assets'].max()
print(f2.head(5))
print('------------------------')
f1['new_name2'] = f1['Ticker Symbol'].apply(lambda x: x.lower())  # apply新增列，可调用函数
print(f1.loc[slice(None), 'new_name2'])  # 查询new_name2这一列，先用slice（None）
"""
#查询new_name2这一列，先用slice（None）
选择所有行，再用列名指定查找的列，
"""
print('----------------------')


def trans(x):
    list1 = x.split('-')
    year, month, day = list1[0], list1[1], list1[2]
    return f'{year}年{month}月{day}日'


f1['日期'] = f1['Period Ending'].apply(trans)
print(f1.loc[slice(None), '日期'])
print('-------------------------')
df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
print(df.head(3))
# df2 = df.apply(np.sqrt)#对Dataframe类型使用，创建一个新的Dataframe
# print(df2)
print('00000000000000000000')
df3 = df.unstack()
print(df3)
