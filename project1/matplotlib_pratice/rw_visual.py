import matplotlib.pyplot as plt

from random_walk import Randomwalk


#只要程序处于活动状态，就不断地模拟随机漫步
while True:
    rw = Randomwalk(500000)
    rw.fill_walk()

    #设置绘图窗口的尺寸
    plt.figure(figsize=(10,6))
    point_numbers = list(range(rw.num_points))
    #使用scatter绘制散点图
    #plt.plot(rw.x_values,rw.y_values,linewidth = 0.5)
    plt.scatter(rw.x_values,rw.y_values,c=rw.y_values,cmap=plt.cm.Blues,s=0.1)
    #突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100 )
    plt.scatter(rw.x_values[-1], rw.y_values[-1], edgecolors='none', s=100)
    plt.show()

    keep_running = input('Make another walk?(y/n): ')
    if keep_running == 'n':
        break