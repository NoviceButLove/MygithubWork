'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''
pi = 'pi_digits.txt'
aoligei = 'aoligei.txt'
with open(aoligei,encoding='UTF-8') as file_object:
    contents1 = file_object.read()
    print(contents1)
print('-------------------------------------')
with open(pi) as file_object:
    for line in file_object:
        print(line,end='')
print('\n-------------------------------------')
line = []
with open(pi) as file_object:#readlines 返回的是列表，readline 返回的是字符串
    line = file_object.readlines()
    print(type(line))
    for lines in line:
        print(lines.rstrip())
print('-----------------------------------------')
pi_2 = ''
for lines in line:
    pi_2 += lines.strip()
print(pi_2.rstrip())
print(len(pi_2.rstrip()))
print('------------------------------------------')