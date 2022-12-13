import itertools
from datetime import datetime, date, time
import re
import numpy as np

dt = datetime(2022, 12, 12, 23, 43, 22)
print(dt.day)
# print(dt.date())

# strftime 方法将datatime转换为字符串
format1 = dt.strftime('%m月%d日%Y年 %H:%M')
print(format1)

# strptime 将字符串转换成datetime对象
print(datetime.strptime('20221212', '%Y%m%d'))  # 注意前后格式一致性
"""
例：'2022-12-23', '%Y-%m-%d'
"""
"""如下，enumerate方法，对可迭代对象，使用，i用于计数"""
a_list = ['liang', 'zhang', 'liu', 'zhou']
mapping = {}
for i, v in enumerate(a_list):
    mapping[v] = i
print(mapping)

# lambda 的一种用法


def applyj_to_list(a_list, f):
    return [f(x) for x in a_list]


list1 = ['jay zhou', 'eason chen', 'CXK']
print(applyj_to_list(list1, lambda x: x.title()))

"""
python 生成器，减少数据内存使用
"""
generator = (x**2 for x in range(101))
print(generator)  # here you can check out that it was a generator object
"""在需要时迭代取出"""
for x in generator:
    print(x)
print('----------------------------------------')
"""itertools库, 以及it而tool迭代器的使用演示"""

first_letter = lambda x: x[0]
names = ['Alan', 'Jay zhou', 'Eason chen', 'Liang Jincheng', 'ZhangPing']
"""letter, names 在  迭代器 groupby 对names采用first_letter分组后的"""
for letter, names in itertools.groupby(names, first_letter):
    """groupby 用first_letter的方式分组， 对象是names"""
    print(letter, list(names))  # names(指代for后面那个)是一个生成器
print('------------------------------------------------')


