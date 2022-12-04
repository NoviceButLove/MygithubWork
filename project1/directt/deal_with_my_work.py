'''定义方法，作为模块'''
def txt_split(file_place,destination):
    '''处理文本文档文件，将其输出为标记格式'''
    with open(file_place, encoding='UTF-8') as file1:#打开该文件，UTF-8 因为是中文
        deal = file1.read().split('\n')#读取
    #deal = deal.split('\n')#分割每一行
    with open(destination,'w') as file2:
        for ii in range(0, len(deal)):#循环遍历列表分割后每一项
            for tst in deal[ii]:#循环遍历字符串每个字
                file2.write(tst+' \n')#打印
            file2.write('\n')#每一条完成后，加一个空格

if __name__ == '__main__':
    plus = r'C:\Users\86151\Desktop\门店名称-PLUS.txt'
    with open(plus, encoding='UTF-8') as file1:
        deal = file1.read().split('\n')
    #deal = deal.split('\n')
    for ii in range(1, len(deal)):
        for tst in deal[ii]:
            print(tst)
        print('')
