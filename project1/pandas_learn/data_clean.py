import pandas as pd

f1 = pd.read_excel(r'C:\Users\86151\Desktop\File_Test\enligh_test.xlsx')
#print(f1.head(3))
#print(f1[:].isnull())是否为空，空返回True

#print(f1.loc[f1['性别'].isnull(),:])
print(f1.loc[3819,:])
f1.dropna(axis=0,how='all')#清理所有的行，行全是空值的
f1.dropna(axis=1,how='all')#清理所有的列，列全是空值
f1.loc[:,'我的练习时长'] = f1['我的练习时长'].fillna(0)
print('============================')
print(f1.loc[f1['姓名'].isnull(),:])
print('---------------------------------')
print(f1.loc[186,'姓名'])
print(f1.loc[2964,'姓名'])
#print(f1.loc[1,'姓名'])#注意，excel开头被认为是columns，然后从0开始读
print('-------------------------')
#print(f1.columns)
print(f1['院系'].dtypes)
f1.dropna(axis=0, how='any',inplace=True)
d2 = f1['院系'].str.startswith('经济管理')
print(f1[d2])#直接放入表达式查询
print('----------000000000000======================')
print(d2)
print('---------------------------------')
d1 = f1['我的练习完成度'].sort_values(ascending=False)
print(d1)
print('-----------------------------')


f1.to_excel(r'C:\Users\86151\Desktop\Temporary_Work\clean_enlish_test.xlsx',index=False)


