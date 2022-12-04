import matplotlib.pyplot as plt

x_values = list(x for x in range(1,5001))
y_values = [y**3 for y in x_values]

plt.scatter(x_values,y_values,c = y_values,s = 15)
plt.title('Number 3 ')
plt.xlabel('X_values')
plt.ylabel('Y_values')
plt.tick_params(labelsize = 14)
plt.axis([0,5100,0,150000000000])
plt.show()
