import pandas as pd
import numpy as np
frame1 = pd.DataFrame({'data1': np.random.randn(1000),
                       'data2': np.random.randn(1000)})
quartiles = pd.cut(frame1.data1, 4)  # 桶，切成4桶
print(quartiles[:10])
print('-----------------')

def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}


grouped = frame1.data2.groupby(quartiles)
print(grouped.apply(get_stats).unstack())
