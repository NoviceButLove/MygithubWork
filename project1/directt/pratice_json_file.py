import json

number = [1,2,3,4,5,4,5,3,5,66,7,7,8,8,8,2208]
json_file1 = 'number_json_file'
with open(json_file1,'w') as file_1:
    json.dump(number,file_1)
print('---------------------------------------')
with open(json_file1,'r')as file1:
    content = file1.read()#返回一个字符串
    print(content)
    print(type(content))
    print('----------------------')
for ii in content:
    print(ii)
