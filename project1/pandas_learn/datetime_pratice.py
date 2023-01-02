from datetime import datetime
import numpy as np
import pandas as pd
import pytz

print(datetime.now())
"""长 时间序列"""
longer_ts = pd.Series(np.random.randn(1000),
                      index=pd.date_range('2021/3/10', periods=1000))
print(longer_ts)
print(longer_ts['2022'])
print(longer_ts['2022-05'])
print(longer_ts[datetime(2022, 1, 3): datetime(2022, 6, 10)])
print('-------------------------------------')
print(pd.date_range('2021-04-04 12:34:21', periods=20, freq='BMS'))
"""时区处理"""
print(pytz.common_timezones[-5:])
"""频率转换"""
time1 = pd.period_range('2019', '2022', freq='A-DEC')
data1 = pd.Series(np.random.randn(len(time1)), index=time1)
print(data1)
print(data1.asfreq('M', how='start'))
min1 = pd.date_range('2022-12-23 02:00:04', periods=12, freq='T')
data2 = pd.Series(np.arange(len(min1)), index=min1)
print(data2)
"""降采样，resample"""
print(data2.resample('5min', closed='right').mean())
"""一行表达式"""
b = input()
c = input()
a = (b if b > c else c)
print(a)
