import requests
from bs4 import BeautifulSoup
from lxml import etree

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# soup_lxml = BeautifulSoup(html_doc, "lxml")

# 第一个a标签的节点
# print("##" * 10, soup_lxml.a)


# selector = etree.HTML(html_doc)
# links = selector.xpath("//p[@class='story']/a/@href")
# for link in links:
#     print(link)

r = requests.get("http://iguye.com/books.xml")
se = etree.HTML(r.text)

print(se.xpath("//book"))

# 选取书店下第一本书的标题
print(se.xpath("//bookstore/book[1]/title/text()"))
# 选取书店下最后一本书的标题
print(se.xpath("//bookstore/book[last()]/title/text()"))
# 选取书店下倒数第二本书的标题
print(se.xpath("//bookstore/book[last()-1]/title/text()"))
# 选取书店下前两本书的标题
print(se.xpath("//bookstore/book[position()<3]/title/test()"))
# 选取所有的分类为web的书本
print(se.xpath("//book[@category='web']/title/text()"))

# 选取所有价格大于30.00元的书本
print(se.xpath("//book[price>35.00]/title/text()"))