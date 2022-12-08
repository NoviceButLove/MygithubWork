import pandas as pd
import numpy as np

film_data = r'C:\Users\86151\Desktop\File_Test\Netflix\Best Movie by Year Netflix.csv'
fm = pd.read_csv(film_data)
# print(fm.head())
# print(fm.describe())
fm1 = fm.dropna(axis=0, how='any')
#print(fm1.describe())
print(fm1.columns)
fm3 = fm1.sort_values('SCORE',ascending=False)
print(fm3.head(3))
print('-------------------------')
#fm2 = fm1.groupby(['SCORE', 'MAIN_PRODUCTION'])['SCORE'].agg([np.max, np.mean, np.min])
#print(fm2.head(3))
print('000---------------------------00000000')
fm4 = fm1.groupby('SCORE').agg(np.max)
print(fm4.head(3))
print('000000000000000000000000000000000000')
fm2 = fm1.loc[slice(None), ['MAIN_PRODUCTION', 'MAIN_GENRE', 'SCORE']]
print('---------------------------------')








