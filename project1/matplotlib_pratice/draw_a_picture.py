import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # matplotlib的图像位于Figure
plt.subplot(221)  # 创建一个2*2的画板，选中第一个
plt.plot(np.random.randn(60).cumsum(), 'k--')
plt.show()
