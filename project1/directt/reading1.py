book1_pg = r'C:\Users\86151\Desktop\pg11.txt'
try:
    with open(book1_pg,encoding='UTF-8') as file_object:
        contents= file_object.read()
        word_bank = contents.split()
except FileNotFoundError:
    print('Sorry ,please provide a correct destination of file')
else:
    print('THE BOOK is ' +str(len(word_bank))+' LONG')
