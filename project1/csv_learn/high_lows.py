import csv

filename1 = r'C:\Users\86151\Desktop\File_Test\sitka_weather_2018_full.csv'  # 全版数据
filename2 = r'C:\Users\86151\Desktop\File_Test\sitka_weather_07-2018_simple.csv'  # 简单版数据
with open(filename1) as f1:
    reader = csv.reader(f1)  # 创建一个阅读器, 放在reader
    hearder_row = next(reader)  # 传入阅读器，返回文件的下一行
    # for index, column_header in enumerate(hearder_row):  # enumerate 获取每个元素的索引和及其值
    #     print(index, column_header)
    print('------------------------------------')
# 从文件中获取最高气温
    highs = []
    for row in reader:
        high = row[8].replace(' ', '')
        highs.append(int(high))
    print(highs)
    print(type(highs[1]))
    # print(type(highs[1]))

