mything = ['iphone','guitar','book','earpods','stucard']
upgrate = []
def newton():
    while mything:
        upgtating = mything.pop()
        print('We are upgrating the '+upgtating+ ' Now...')
        upgrate.append(upgtating)
    print('Now your thing have been uprated')
    for thing in upgrate:
        print(thing,end='\t')

newton()