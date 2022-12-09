import pandas as pd
import numpy as np

film_data = r'C:\Users\86151\Desktop\File_Test\Netflix\Best Movie by Year Netflix.csv'
fm = pd.read_csv(film_data)
# print(fm.head())
# print(fm.describe())
fm1 = fm.dropna(axis=0, how='any')
# print(fm1.describe())
print(fm1.columns)  # 查看列名
fm3 = fm1.sort_values('SCORE', ascending=False)  # 排序，按SCORE，降序
print(fm3.head(3))  #
print('-------------------------')
# fm2 = fm1.groupby(['SCORE', 'MAIN_PRODUCTION'])['SCORE'].agg([np.max, np.mean, np.min])
# print(fm2.head(3))
print('000-----------按生产商分组，查看分数最大值----------------00000000')
fm4 = fm1.groupby('MAIN_PRODUCTION').agg(np.max)
print(fm4)
print('00000000000000000查看所有行，看生产商，类型个，分数三列0000000000000000000')
fm2 = fm1.loc[slice(None), ['MAIN_PRODUCTION', 'MAIN_GENRE', 'SCORE']]
print(fm2)
print('---------------------------------')
