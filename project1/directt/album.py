abl1 = {}
#kaiguan = 1#当你不想把函数中需要存储的变量内容刷新时，你需要提前定义他，如上
#但是，想这个开关，你就需要定义在函数内，因为他是为函数服务的，而函数为abl1服务
def abl(nam = 'Ablum'):
    kaiguan = 1
    while True:

        if kaiguan == 1 :
            nam = input('Please enter a ablum you like: ')
            singer = input('Please enter the singer of the ablum you enter: ')
            abl1[nam] = singer
            kaiguan = input("Still playing (yes/no)")
            if kaiguan == 'no':
                kaiguan = 0
            else:
                kaiguan = 1
        else:
            break
    for a,b in abl1.items():
        print('Name: '+str(a)+'\t'+'Singer: '+str(b))
abl('ablum')