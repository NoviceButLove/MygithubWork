import pandas as pd
import openpyxl
file1 = pd.read_excel(r'C:\Users\86151\Desktop\File_Test\pandas_test.xlsx')
#print(file1.head())
print('--------------------')

print(file1.loc[:, '日期'])
print('----------------')
print(file1.index)
print(file1.columns)
#file1.loc[:, '日期'] = file1['日期'].str.replace('-', '')这里数据有问题，所以报错，datatime的数据
#print(file1)
#file1.set_index()可以设置列索引
print(file1.loc[23,'姓名'])#用行坐标加列坐标确定
print('----------------------------')
print(file1.loc[file1['疫情风险等级'] == '常态化防控地区', :])

