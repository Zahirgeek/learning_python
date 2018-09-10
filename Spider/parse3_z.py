# 本案例是利用Request来实现parse2_z.py的内容
from urllib import request, parse

import json

baseurl = "http://fanyi.baidu.com/sug"
kw = input("输入查询的单词: ")
data = {
    "kw": kw
}

data = parse.urlencode(data).encode("utf-8")

headers = {
    "Content-Length": len(data)
}
# 构造一个Request实例
req = request.Request(url=baseurl, data=data, headers=headers)

rsp = request.urlopen(req)

json_data = rsp.read().decode()
dict_data = json.loads(json_data)

for item in dict_data["data"]:
    print("{0}------>{1}".format(item["k"], item["v"]))