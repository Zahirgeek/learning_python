import json
import urllib.request

r = urllib.request.urlopen("http://httpbin.org/get")

# 读取response的内容
text = r.read()

# http返回状态码和msg
print(r.status, r.reason)

# 返回的内容是json格式,直接用load函数加载
obj = json.loads(text)
print(obj)

# r.headers是一个HTTPMessage对象
for k, v in r.headers._headers:
    print("{0}: {1}".format(k, v))

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
# 添加自定义请求头信息
req = urllib.request.Request("http://httpbin.org/user-agent")
req.add_header("User-Agent", ua)
# 接收一个urllib.request.Request对象作为参数
r = urllib.request.urlopen(req)
resp = json.load(r)
# 打印出httpbin网站返回信息里的user-agent
print("user-agent: ", resp["user-agent"])
print("########################################################")

########################################################

# 发起带basic auth的请求
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm="Fake Realm",
                          uri="http://httpbin.org",
                          user="zahir",
                          passwd="12306")
opener = urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)
r = urllib.request.urlopen("http://httpbin.org/basic-auth/zahir/12306")
print(r.read().decode("utf-8"))

########################################################

# 使用GET参数
params = urllib.parse.urlencode({"spam": 1, "eggs": 2, "bacon": 1})
url = "http://httpbin.org/get?{0}".format(params)
with urllib.request.urlopen(url) as f:
    print(json.load(f))

print("################################")
#
# # 使用POST方法传递参数
data = urllib.parse.urlencode({"name": "小明", "age": 2})
data = data.encode()
with urllib.request.urlopen("http://httpbin.org/post", data) as f:
    print(json.load(f))

print("################################")

################################

# 代理IP请求远程url
proxy_handler = urllib.request.ProxyHandler({
                    "http": "http://47.106.138.135:41801"
                })

opener_za = urllib.request.build_opener(proxy_handler)
r = opener_za.open("http://httpbin.org/ip")
print(r.read().decode("utf-8"))



