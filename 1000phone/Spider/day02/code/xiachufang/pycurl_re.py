# pycurl和正则实现爬取下厨房的图片
import os
import re
from io import BytesIO
from urllib.parse import urlparse
from pycurl import Curl

buffer = BytesIO()
c = Curl()
c.setopt(c.URL, "http://www.xiachufang.com/")
# 使用代理
# c.setopt(c.PROXY,'http://')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
body = buffer.getvalue()
text = body.decode("utf-8")

img_list = re.findall(r'src=\"(http://i[1-2]\.chuimg\.com/\w+\.jpg)', text)
print(img_list)

image_dir = os.path.join(os.curdir, "images")

for img in img_list:
    o = urlparse(img)
    filename = o.path[1:]
    filepath = os.path.join(image_dir, filename)
    # 初始化下载目录
    if not os.path.isdir(os.path.dirname(filepath)):
        os.mkdir(os.path.dirname(filepath))
    url = "%s://%s/%s" % (o.scheme, o.netloc, filename)
    print(url)
    with open(filepath, "wb") as f:
        c = Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, f)
        c.perform()
        c.close()
