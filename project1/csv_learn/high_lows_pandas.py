import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

filename2 = r'C:\Users\86151\Desktop\File_Test\sitka_weather_07-2018_simple.csv'  # 简单版数据
file1 = r'C:\Users\86151\Desktop\File_Test\sitka_weather_2018_full.csv'
#f1 = pd.read_csv(file1)
f1 = pd.read_csv(filename2)
print(f1.columns)
f1.dropna(axis=0, how='any')
high = f1.loc[slice(None), 'TMAX']
date = f1.loc[slice(None), 'DATE']
low = f1.loc[slice(None), 'TMIN']
print(high.head(3))
dates, highs, lows = [], [], []
for data in high:
    highs.append(data)
for data1 in date:
    dates.append(data1)
for data in low:
    lows.append(data)
times = []
print(highs[: -100])
print(dates[: 5])
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(13, 12))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows,c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置图形的格式
plt.title('Daily high and low temperatures', fontsize=24)
plt.xlabel('', fontsize=1)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
d1 = datetime.strptime('2014-7-01', '%Y-%m-%d')
print(d1)
