import torch
print(torch.cuda.is_available())
a = (10,20)
b = ((10,20),(20,30))
c = a is b[1]#is 可以返回一个布尔值，元组中的只可以进行比较
print(c)