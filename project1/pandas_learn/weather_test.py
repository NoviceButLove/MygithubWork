import pandas as pd

# 设置查看
# #显示所有列
# pd.set_option('display.max_columns', None)
# #显示所有行
# pd.set_option('display.max_rows', None)
# #设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth',100)


name = r'C:\Users\86151\Desktop\File_Test\weather\testset.csv'
f1 = pd.read_csv(name)  # 读取1000行
f1.dropna(axis=0, how='any')  # 预处理，除去有空的行
print('--------------_wgustm 的空值----------------------')
print(f1.loc[f1[' _wgustm'].notnull() |
             f1[' _windchillm'].notnull()])  # 条件查找
print('----------datatime_utc分组--------------')
print(f1.head(3))
print(f1['datetime_utc'].dtypes)
print(f1.columns)
f2 = f1.groupby('datetime_utc')
print(f2.head(3))  # 分组，按时间
print('------------分组，按时间, conds-----------------')
f2 = f1.groupby(['datetime_utc', ' _conds'])
print(f2.head(3))
print('------------- 1996 到 2004 年的数据-------------------------')
f1.set_index('datetime_utc')  # 直接调整Dateframe的index
print(f1.loc['19961101-11:00':'20041101-11:00'])
print('=========数据描述==============')
print(f1.describe())
print('-------------------天气类型计数--------------------------')
print(f1[' _conds'].value_counts())
print('-----------协方差-----------')
print(f1.cov())
print('----------------相关系数--------------------')
print(f1[' _hum'].corr(f1[' _dewptm']))
print('000000000000000000000000000000000000000')
f1['datetime_utc'] = f1['datetime_utc'].str[:-6]  # 用str的切片语法
# f1['datetime_utc'].reset_index()
# print(f1.head(3))
print('000000000000000000000000000000000000')


def change_date(x):
    """转换时间"""
    x_year = x['datetime_utc'][0:4]
    x_month = x['datetime_utc'][4:6]
    x_day = x['datetime_utc'][6:8]
    return f"{x_year}年{x_month}月{x_day}日"


f1['日期'] = f1.apply(change_date, axis=1)
print(f1.head(3))
print(type(f1['datetime_utc']))
print('0000000000000-----loc()条件查找法----------0000000000')
f5 = f1.loc[f1[' _heatindexm'].notnull()]
print(f5.head(3))
print('-----------2022/12/15')
print(f1.head(5))
f2 = pd.read_csv(name, chunksize=1000)  # nrows= 用于指定读取多少行
#  chunksize 逐行读取，读取全部
conds = pd.Series([], dtype='float64')
for cond in f2:
    conds = conds.add(cond[' _conds'].value_counts(), fill_value=0)
conds = conds.sort_values(ascending=False)
print('-----------------------')
print(conds)



