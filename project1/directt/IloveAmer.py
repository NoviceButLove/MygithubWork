def gowhelike(*like3,like='American'):
    print('I like '+like+' most')
    like3 = list(like3)
    for like3 in like3:
        print('I like '+like3+' second')
gowhelike('China','Japan',like='Africa')