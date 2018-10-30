# bs4爬取下厨房图片
import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.xiachufang.com/')
soup = BeautifulSoup(r.text)

img_list = []
for img in soup.select('img'):
    if img.has_attr('data-src'):
        img_list.append(img.attrs["data-src"])
    else:
        img_list.append(img.attrs['src'])

image_dir = os.path.join(os.curdir, "images")
# if not os.path.isdir(image_dir):
#     os.mkdir(image_dir)

for img in img_list:
    o = urlparse(img)
    filename = o.path[1:].split("@")[0]
    filepath = os.path.join(image_dir, filename)
    # 初始化下载目录
    if not os.path.isdir(os.path.dirname(filepath)):
        os.mkdir(os.path.dirname(filepath))
    url = "%s://%s/%s" % (o.scheme, o.netloc, filename)
    resp = requests.get(url)
    with open(filepath, "wb") as f:
        for chunk in resp.iter_content(1024):
            f.write(chunk)