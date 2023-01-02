import numpy as np

data1 = [6, 6, 2, 23, 0, 1]
arr1 = np.array(data1)
print(arr1)
print('check2')
print(arr1[1])
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)  # 嵌套序列，比如等长列表组成的列表
print('check')
print(arr2)  # numpy 自动将他们对齐了
print('check1')
print(arr2[1])
print(arr2.shape)  # 看形状 -> (2, 4) 元祖
print(np.zeros((5, 6)))  # 创建一个全是0 的5行6列的数组, 6 后面还有个数的参数
print('--------------------------------')
"""numpy 对数组的标量数学运算和应用到每一个元素上"""
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
print(arr**2)
print(1/arr)
arr2 = np.array([[9., 4., 6.], [1., 4., 3.]])
print(arr2 > arr)
"""不同数组之间的运算叫做广播"""
"""numpy对数组的操作直接改变源数组，需要用.copy()来进行复制操作"""
# 对n维数组，可以用n个[]取值，或[, , ,]形式填入坐标值
"""     n维数组，可用切片取值取行列，
        [[，，]]表示n维数组中
        第0行的某某列
        [:, [,,]]
        表示第1行的某某列
        以此类推
"""
arr2_1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2_1[1])  # [4, 5, 6]
print(arr2_1[0][2])  # 3

"""布尔型索引"""
names = np.array(['Bob', 'Joe', 'Liang', 'Zhang', 'Bob', 'Liu', 'Zhou'])
data1 = np.random.randn(7, 5)  # 一个7行5列的数组
print(data1[names == 'Bob'])  # 输出data1中True的行
#  !=  <==>  ~  反转条件
"""numpy 对数组的操作是有合并"""
