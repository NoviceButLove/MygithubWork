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
print('-------------------------')
print(file1.loc[23,'姓名'])#用行坐标加列坐标确定
print('----------------------------')
'''下面函数，逗号前参数是行，后是列'''
print(file1.loc[file1['疫情风险等级'] == '常态化防控地区', '姓名':'学号'])
print('-----------------------')
'''
前行后列，下面函数loc，选择所有行，
列，若不存在则创建一个新列’分数‘
进行赋值
'''
file1.loc[:,'分数'] = 100
print(file1.loc[file1['疫情风险等级'] == '常态化防控地区', '姓名':'分数'])

#print(file1.head())
print('--------------------')
'''
下面是loc的另一种创建列，加上series的方式
loc[：->选择所有行 ，’新列的名称‘]apply（函数名，坐标轴）
'''
def plus_score(df):
    if df['疫情风险等级'] == '常态化防控地区':
        return 'good'
    else:
        return 'so-so'
file1.loc[:, 'plusscore'] = file1.apply(plus_score, axis=1)
print(file1.head())
#print(file1)
print('-----------------------------')
print(file1['plusscore'].value_counts())#查看plusscore 枚举结果的个数
print(file1['plusscore'].value_counts('so-so'))#查看plusscore 指定结果的百分比

print('-------------------------')

#print(file1.describe())
print(file1['plusscore'].unique())#查看独特值
print(file1['plusscore'].value_counts())#各个值计数
'''
file1.cov()协方差矩阵
file1.corr()相关系数矩阵 
！！！！数据挖掘后（计算特定的方差或系数）可用作于机器学习
'''










