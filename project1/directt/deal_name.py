import pandas as pd
import random
#import numpy as np #无用导入
dates_DIS1 = pd.read_csv(r"D:\LJCWork\BeginWithTechnique\independ_Work_22-11-11\name-DIS(1).txt",
                        header = None,                              #参数不是很懂
                        sep = r'\n',                                #此处看不懂,但是知道用于读取数据
                        engine='python')
dates_DIS2 = pd.read_csv(r"D:\LJCWork\BeginWithTechnique\independ_Work_22-11-11\门店名称-PLUS.txt",
                        header = None,                              #参数不是很懂
                        sep = r'\n',                                #此处看不懂,但是知道用于读取数据
                        engine='python')
'''for ii in range(0,600):
    rand=random.randint(0,4613)#创建随机数
    str1=list(dates_DIS1.loc[rand])#集合化数据,使用集合的格式,规避原始dateframe的格式
    str2=str(str1)#进一步规整数据为string型,方便后续处理
    begi=len(str2)-2#计算每一个名称的长度,-2 是为了出去集合型自带的 [' 和 ']
    for item in range(2,begi):#使用循环,跳过了['开始读取
        print(str2[item],end='\n')#每次输出一个就换行,
    print(end='\n')#最后输出完,补一个换行
'''
#门店名称-PLUS
for ii in range(0,600):
    rand=random.randint(0,40469)#创建随机数
    str1=list(dates_DIS2.loc[rand])#集合化数据,使用集合的格式,规避原始dateframe的格式
    str2=str(str1)#进一步规整数据为string型,方便后续处理
    begi=len(str2)-2#计算每一个名称的长度,-2 是为了出去集合型自带的 [' 和 ']
    for item in range(2,begi):#使用循环,跳过了['开始读取
        print(str2[item]+' ',end='\n')#每次输出一个就换行,
    print(end='\n')#最后输出完,补一个换行






