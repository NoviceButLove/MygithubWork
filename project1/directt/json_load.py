import json

file = 'number_json_file'
with open(file) as file1:
    file2=json.load(file1)
    print(file2)