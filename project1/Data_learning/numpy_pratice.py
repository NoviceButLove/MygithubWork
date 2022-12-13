import numpy as np

data1 = [6, 6, 2, 23, 0, 1]
arr1 = np.array(data1)
print(arr1)
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)  # 嵌套序列，比如等长列表组成的列表
print(arr2)  # numpy 自动将他们对齐了
print(arr2.shape)  # 看形状 -> (2, 4) 元祖
print(np.zeros((5, 6)))  # 创建一个全是0 的5行6列的数组, 6 后面还有个数的参数



