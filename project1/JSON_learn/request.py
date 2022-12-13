import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print('Total repositories:', response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']  # item这个列表，里面是字典型数据
print('Repositories returned:', len(repo_dicts))  # 打印列表长度，查看仓库数量

# 研究第一个仓库
repo_dict = repo_dicts[0]  # 取出第一个仓库
print('\nKeys:', len(repo_dict))  # 换行，输出该字典中有多少键值对
for key in sorted(repo_dict.keys()):  # 取出排列后的第一个仓库的每一个key值
    print(key)  # 打印所有键值对


# 处理结果
print(response_dict.keys())
