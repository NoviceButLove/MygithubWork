import pandas as pd
import matplotlib as mpl

#设置查看
# #显示所有列
# pd.set_option('display.max_columns', None)
# #显示所有行
# pd.set_option('display.max_rows', None)
# #设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth',100)


name = r'C:\Users\86151\Desktop\File_Test\weather\testset.csv'
f1 = pd.read_csv(name)#读取
f1.dropna(axis=0, how='any')#预处理，出去有
# 空值得行
print('--------------_wgustm 的空值----------------------')
#print(f1.loc[f1[' _wgustm'].isnull(), :])
print('------------------------')
print(f1.head(3))
print(f1.columns)
f1.groupby('datetime_utc')
print(f1.head(3))#分组，按时间
print('-----------------------------------')
#f2 = f1.groupby([f1['datetime_utc'],f1[' _conds']])
#print(f2.head(3))
f1.set_index('datetime_utc')
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
f1['datetime_utc'] = f1['datetime_utc'].str[:-6]#用str的切片语法
#f1['datetime_utc'].reset_index()
#print(f1.head(3))
print('000000000000000000000000000000000000')
def change_date(x):
    x_year = x['datetime_utc'][0:4]
    x_month = x['datetime_utc'][4:6]
    x_day = x['datetime_utc'][6:8]
    return f"{x_year}年{x_month}月{x_day}日"
f1['日期'] = f1.apply(change_date, axis=1)
print(f1.head(3))
print(type(f1['datetime_utc']))
print('0000000000000---------------0000000000')
f5 = f1.loc[f1[' _heatindexm'].notnull()]
print(f5.head(3))