import  json

love_num_file = 'love_number.json'


def check_love_num():
    '''判断是否存在目标数字'''
    with open(love_num_file) as file1:
        num1 = str(json.load(file1))
        print('Is this your favourite number? -> ' + num1)
        responce1 = input('Enter yes/no to check -> ')
        if responce1 == 'yes':
            return True
        elif responce1 == 'no':
            return False
        else:
            print('Sorry ,I don\'t understand what do you mean. ')
            check_love_num()

def get_love_number():
    '''得到所需的数字'''
    try:
        file_love = open(love_num_file, 'w')
        num = int(input('Please enter your favourite number: '))
    except ValueError:
        print('Please enter a number!!')
        get_love_number()
    else:
        num2 = str(num)
        json.dump(num2, file_love)  # json.dump()不接受int，接受str
        file_love.close()


def print_num():
    '''打印结果 '''
    try:
        with open(love_num_file) as file_love:
            num = str(json.load(file_love))
    except FileNotFoundError:
         print('Sorry ,we didn\'t find the file in dict')
    else:
        print('I know your favorite number! It’s ->> ' + num )


def game_love_num():
    '''主程序'''
    judge_num = check_love_num()
    if judge_num:
        print_num()
    else:
        get_love_number()
        print_num()



if __name__ == '__main__':
    game_love_num()
