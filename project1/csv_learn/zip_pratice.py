import json
import pandas as pd

f1 = pd.read_csv(r'C:\Users\86151\Desktop\File_Test\population\world_population.csv')
print(f1.head(3))
header = f1.loc[slice(None), 'Country/Territory']
value = f1.loc[slice(None), 'Growth Rate']
data_dict = dict(zip(header, value))
print(data_dict)
file_JSON = r'C:\Users\86151\Desktop\File_Test\JSON\dev-v1.1.json'
data1 = pd.read_json(file_JSON)
print(data1)