from die import Die
import pygal
from die import x_label

#创建一个D6
die = Die()

die.roll(10000)

#对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 10000 times.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', die.cal_frequency())
hist.render_to_file('die_visual.svg')















