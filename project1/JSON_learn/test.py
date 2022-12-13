import json
from datetime import fromtimestamp

# 将数据加载
filename = r'D:\LJCWork\BeginWithTechnique\book_data_pycharm\ehmatthes-pcc_2e-078318e\chapter_16\mapping_global_data_sets\data\eq_data_7_day_m1.json'
with open(filename) as f:
    eq_data = json.load(f)
    print(datetime.fromtimestamp(eq_data['time']))
# for eq_dict in eq_data:
#     if datetime.fromtimestamp(datetime.fromtimestamp()) :
