import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

place = 'http://www.pythonscraping.com/pages/page3.html'
local_place = "file:///D:/File_Test/hfhtmlcss/chapter5/mypod/index.html"
html = urlopen(place)
# print(html.getcode())
bsobj1 = BeautifulSoup(html.read(), features='lxml')
print(bsobj1)
print('----------------')
print(bsobj1.findAll("h1"))
print('--------------------')
# place = 'http://www.pythonscraping.com/pages/page3.html'
# html1 = urlopen(place)
# bsobj = BeautifulSoup(html1)
# for child in bsobj.find('table', {'id':'giftList'}).children:
#     print(child)
"""正则表达式"""
bsobj2 = BeautifulSoup(html)
# images = bsobj2.findall('img', {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})

