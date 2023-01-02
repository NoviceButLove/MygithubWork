import pygal

from die import Die
from die import cal_x_label as cxl


# 创建两个D6骰子
die_1 = Die()
die_2 = Die()
die_3 = Die(6)

# 掷多个骰子多次， 并将操作结果存储到一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling three D6 1000 times.'
hist.x_labels = []
hist.x_labels.extend(cxl(die_1, die_2, die_3))
# 分析结果

def cal_frequencies(*die):
    """同，计算范围"""
    frequencies = []
    max_num = 1
    min_num = 0
    for num_die in die:
        max_num += num_die.num_facet
        min_num += 1
    for value in range(min_num, max_num):
        frequency = results.count(value)
        frequencies.append(frequency)
    return frequencies


hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('Three D6', cal_frequencies(die_1, die_2, die_3))
hist.render_to_file('dicd_visual.svg')
