import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap = plt.cm.Blues,edgecolors='none',s=25)#实参s 指定点的大小
'''
edgecolor = 'none' 设定轮廓颜色为无，点的颜色默认为蓝色
将y_values 赋值给c ，可使点在不同值间颜色不同
cmap 则将颜色指定为某种特设颜色
'''
#设置图表标题并给坐标轴加上标签
plt.title('Square Numbers',fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel('Square of Value',fontsize = 14)
#设置刻度标记的大小
plt.tick_params(axis='both',which = 'major',labelsize = 14)

#设置每个坐标轴的取值范围
plt.axis([0,1100, 0 , 1100000])

plt.show()
#plt.savefig('squares_plot.png',,bbox_inches = 'tight')
'''savefig 第一个参数指定以什么文件名保存文件，第二个参数将多余的空白区域裁剪掉'''
