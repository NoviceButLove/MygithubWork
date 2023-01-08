dict1={2208:1,'8802':'666'}#int str  can use to be key
dict2=dict(c=3,d='world')
print(dict1,type(dict1))
print(dict2,type(dict2))
print('-----------------------------------------------')
dict_stuID_2208={'liang':20221111145,'zhang':20221111167}#  {key:value}
dict_gender_2208={'liang':'male','ai':'female'}
dict_classnum={2208:666,2207:520,2203:123}
print(dict_classnum[2208])
print(dict_classnum.get(2207))
print(dict_stuID_2208['liang'])
print(dict_gender_2208.get('ai'))
print(dict_gender_2208.get('a',99))#if the key don't exist, use .get() won't put forward the error Instead , it will print None
#You can put a value after the inexist dict ,just as upon,99 is regarded as the default value
print('-----------------------------------------------------------')
#del dict_stuID_2208['liang']
print(dict_stuID_2208)
print('zhang' in dict_gender_2208)
#dict_stuID_2208.clear()
print(dict_stuID_2208)
dict_gender_2208['ai']='male'#refine or add the value in the dict
print(dict_gender_2208)
'''
The dictionary is similar to list
'''
print('---------------------------------------------------')
ky=dict_stuID_2208.keys()
val=dict_gender_2208.values()
ite=dict_classnum.items()
print(ky)
print(val)
print(ite)
print(list(ky))
print(list(val))
print(list(ite))
print("------------------------------------")
dict3 = {1: 'hello', 2: 'world'}

















