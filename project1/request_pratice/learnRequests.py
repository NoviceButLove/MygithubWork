import requests

print('------------开始--------------')
# # r 是一个Response 对象
# # 要啥就说, PUT、DELETE、HEAD 和 OPTIONS 同理
# r = requests.get('https://api.github.com/events')  # HTTP get 请求 post 请求
html = 'https://httpbin.org'
# r = requests.post(html + '/post', data={'key': 'value'})
# r = requests.put(html + '/put', data={'key': 'value'})
# r = requests.delete(html + '/delete')
# # 在URL中传递参数
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get(html + '/get', param=payload)
# print(r.encoding)  # 查看编码类型
# r.encoding = 'ISO-8859-1'  # 推荐查看编码然后自己编码
# # 每次更改会被Requests记住
print('---------------------------')
# # 自定义数据形式
# payload = {'key1': ['value1', 'value2']}  # 列表形式
# # payload = {('key1': 'value1), ('key1': 'value2')} # 元组形式
# r2 = requests.post('https://httpbin.org/post', data=payload)
# print(r2.text)  # 返回值
print('------------发送文件内容，不懂-----------------')
# files = {'file': open('report.xls', 'rb')}
# r = requests.post(html + '/post', files=files)
# print(r.text)
print('--------------------')
r = requests.get('https://httpbin.org/get')
print(r.status_code)
