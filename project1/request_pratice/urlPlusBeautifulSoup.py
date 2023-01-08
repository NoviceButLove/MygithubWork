from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

# print('-------------基础练习-----------------------')
# html = urlopen("https://pythonscraping.com/")
# soup = BeautifulSoup(html, features="lxml")
# # print(soup.prettify())  # 显示
# print('----------')
# print()
# # print(soup.find_all('p'))  # 找所有的
# print(soup.find('a').get('href'))  # 找<p> 然后得到<href>
# print(soup.get_text())  # 放在<p>里面的内容
# print(soup.attrs)
# print('-----------------')
# # print(soup.p.string)
# # print(type(soup.p))

"""练习2"""
html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(html, features='lxml')
# content = bsobj.find("div", {"id": "mw-content-text"}).get_text()
# content = bytes(content, "UTF-8")
# content = content.decode("UTF-8")
# print(content)
"""BS笔记"""
# print(soup.get_text())  # 获取所有文字内容
# for href in soup.find_all('link'):
#     print(href['href'])  # 操作标签的属性可以像操作字典一样, 也可以是get(..)
#     print()
# 想获取标签的所有属性，就用attrs
# print(soup.find('link').attrs)
print('---------------------')
# 子节点  .descendant .contents .children
for child in soup.title.descendants:  # 寻找每个标签为<head>子孙们
    print(child)
# print(soup)  # html所有内容
print(soup.find_all(['meta', 'link']))  # 列表匹配模式，还有re.compile()正则的用法
"""find_all()参数如下：name , attrs , recursive , string , **kwargs   """
# 第一个是标签名，第二个是标签的属性
#  find_all("p", "title") 返回的是CSS Class为”title”的<p>标签
# 使用 参数的搜索方法搜索参数
print(soup.find_all(id=True))  # 寻找所有有id参数的标签 find_all()括号里面是个布尔值就行
# 使用 class_= 搜索含有CSS参数的标签

# string参数搜索字符串
print(soup.find_all(string='a'))
