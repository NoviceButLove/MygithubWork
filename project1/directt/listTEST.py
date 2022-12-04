abc = {'zeng':666}
cba = ((1,2,3),('123','345','356'))
set1 = {1,2,3,4,5,5,2,53,2,'123','123','2345'}
test1 = [123,'123',abc,cba,set1]
for ite in test1:
    print(type(ite))
    ty = str(type(ite))
    if ty == "<class 'int'>":
        print(ite)
    if ty == "<class 'str'>":
        print(ite.upper())
    if ty == "<class 'dict'>":
        for a in ite.items():
            print(a)
    if ty == "<class 'tuple'>":
        for b in ite:
            print(b)
    if ty == "<class 'set'>":
        print(ite)