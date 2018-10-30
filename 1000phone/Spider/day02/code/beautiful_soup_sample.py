from bs4 import BeautifulSoup
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

soup = BeautifulSoup(html_doc, "html.parser")
print(soup.p)

# 取出第一个p标签下的所有子节点
print(soup.p.children)

soup_find = soup.find(id="link3")
print(soup_find)
print(soup_find.get_text())

# 支持CSS选择器
# 找出class=story的节点
soup.select(".story")
# 找出id=link1的节点
soup.select("#link1")
