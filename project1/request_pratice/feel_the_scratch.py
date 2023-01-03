from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()  # 设置集合去重数据
random.seed(datetime.datetime.now())  # 创建随机数


def getInternalLinks(bsobj, includeUrl):
    """探索内链"""
    internalLinks = []  # 创建列表用于存储
    # 找出所有以“/”开头的链接（内链，相对路径）
    # 每个BS找到的<a>里面的href，符合正则要求的
    for link in bsobj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:  # 如果<a>里面有href
            if link.attrs['href'] not in internalLinks:  # 如果href属性的值 不在 列表中
                internalLinks.append(link.attrs['href'])  # 加入
    return internalLinks  # 返回结果


def getExternalLinks(bsobj, excludeUrl):
    """获得外链，同内链"""
    externalLinks = []
    # 找出以“http”或“www”开头且不包含当前URL的链接
    for link in bsobj.findAll("a",
                              href=re.compile("^(http|www)((?!" +
                                              excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    """处理单个搜素结果，获取其网站名"""
    addressParts = address.replace("http://", "").split("/")  # 得到类似（oreilly.com）的网站名
    return addressParts


def getRandomExternalLink(startingPage):
    """主函数"""
    html = urlopen(startingPage)
    bsobj = BeautifulSoup(html)  # BS常规处理
    externalLinks = getExternalLinks(bsobj, splitAddress(startingPage)[0])  # 对传入的网站名进行处理，然后执行函数
    if len(externalLinks) == 0:  # 如果网站里外链结果为0
        internalLinks = getInternalLinks(startingPage)  # 改为检索内链
        return getExternalLinks(internalLinks[random.randint(0,
                                len(internalLinks) - 1)])  # 然后随机选择内链，再次检索外链
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]  # 迭代


def followExternalOnly(startingSite):
    """启动程序"""
    externalLink = getRandomExternalLink(startingSite)
    print("随机外链是: " + externalLink)
    followExternalOnly(externalLink)  # 迭代


followExternalOnly("http://oreilly.com")
