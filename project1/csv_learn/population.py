import pandas as pd
import matplotlib.pyplot as plt

file = r'D:\File_Test\population\world_population.csv'
data = pd.read_csv(file)
print(data.columns)
data1 = data['Area (km²)'].sort_values(ascending=False)
data2 = data.sort_values(by='Area (km²)', ascending=False)
print(data2['Country/Territory'][:4])
plt.plot(data['CCA3'], data['2022 Population'], linewidth=1)
print(data1.head(3))
plt.show()
