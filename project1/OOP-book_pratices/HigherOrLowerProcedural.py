"""the first program of the book
<Object-Oriented Python_ Master OOP by Building Games and GUIs
[genuine pdf]_Irv Kalb_zhelper-search>"""

import random

# Card constants
SUIT_TUPLE = ('Spades', 'hearts', 'Clubs', 'Diamonds')  # 黑桃、红桃、梅花、钻石
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8',
              '9', 'Jack', 'Queen', 'King')

NCARDS = 8  # 一局游戏进行次数


def getCard(deckListIn):
    """发牌"""
    thisCard = deckListIn.pop()  # 从牌堆顶部取牌
    return thisCard


#  洗牌
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  #
    random.shuffle(deckListOut)
    return deckListOut


#  主程序
if __name__ == "__main__":
    print('Welcome to Higher or Lower.')
    print('You have to choose whether the next card to be shown will be higher or '
          'lower than the current card.')
    print('Getting it right adds 20 points;get it wrong and you lose 15 points.')
    print('You have 50 points to start.')
    print()

    startingDeckList = []  # 空牌堆
    """组装牌，一个花色一张牌，标记属性"""
    for suit in SUIT_TUPLE:  # 每一种牌
        for thisValue, rank in enumerate(RANK_TUPLE):  # enumerate 返回一个枚举对象，包含计数值
            """thisValue 是计数值，从0开始; rank 是参数的值（'Ace', '2'...）"""
            cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
            """此处产出结果为一张牌，rank是‘Ace’, suit是‘黑桃’, value 是 1"""
            startingDeckList.append(cardDict)
    score = 50
#  到此，牌堆已组装完毕
    while True:  # 玩很多局
        # 初始化中...Initialize
        print()
        gameDeckList = shuffle(startingDeckList)  # 调用函数，进行洗牌
        currentCardDict = getCard(gameDeckList)  # 调用函数，进行发牌
        """取出现在这张牌的属性：rank，value，suit"""
        currentCardRank = currentCardDict['rank']
        currentCardValue = currentCardDict['value']
        currentCardSuit = currentCardDict['suit']
        print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
        print()

        for cardNumber in range(0, NCARDS):
            """开始第一轮游戏"""
            answer = input('Will the next card be higher or lower than the ' +
                           currentCardRank + ' of ' +
                           currentCardSuit + ' ? (enter h or l): ')
            answer = answer.casefold()  # 强制小写
            """再次从牌堆顶部取一张牌，并取出属性"""
            nextCardDict = getCard(gameDeckList)
            nextCardRank = nextCardDict['rank']
            nextCardSuit = nextCardDict['suit']
            nextCardValue = nextCardDict['value']
            print('Next card is: ', nextCardRank + ' of ' + nextCardSuit)
            if answer == 'h':
                if nextCardValue > currentCardValue:
                    print('You got it right, it was higher')
                    score += 20
                else:
                    print('Sorry, it was not higher')
                    score -= 15
            elif answer == 'l':
                if nextCardValue < currentCardValue:
                    print('You got it right, it was higher')
                    score += 20
                else:
                    print('Sorry, it was not higher')
                    score -= 15

            print('Your score is: ', score)
            print()
            """比较完毕后，将值传递，开始第二轮猜测"""
            currentCardRank = nextCardRank
            currentCardValue = nextCardValue
        """继续玩下去？"""
        goAgain = input('To play again, press ENTER, or "q" to quit: ')
        if goAgain == 'q':
            break  # 跳出两个循环
    print("OK, bye!")
