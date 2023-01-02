from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())  # 生成随机数


def getLinks(articleUrl):
    """定义函数，用于查找相关链接"""
    html = urlopen("http://en.wikipedia.org" + articleUrl)  # 经典，urlopen 打开网址
    bsobj = BeautifulSoup(html, features="lxml")  # 经典， soup读取网页
    """返回值，找div 属性 bodyContent 下，所有，<a>标签下，href 属性 为（正则表达式）的"""
    return bsobj.find("div", {'id': "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))  # 返回一个列表


links = getLinks("/wiki/Kevin_Bacon")  # 调用函数，赋初值
while len(links) > 0:  # 当结果不为零
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]  # 取列表中的某一条
    links = getLinks(newArticle)  # 继续搜索
