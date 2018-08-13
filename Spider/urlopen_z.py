# 使用urllib.request请求一个网页内容,并把内容打印出来
from urllib import request

if __name__ == '__main__':
    url = "https://jobs.zhaopin.com/390261416251663.htm"
    # 打开相应url并把相应页面作为返回
    rsp = request.urlopen(url)

    # 把返回结果读取出来
    #读取出来的内容类型为bytes
    html = rsp.read()

    # 如果想把bytes内容转成字符串,需要解码
    html = html.decode()
    # 需要以utf-8储存文件,windows默认gbk编码
    with open("url.txt", "w", encoding="utf-8") as f:
        f.write(html)
    print(html)