from urllib import request, parse
'''
掌握对url进行参数编码的方法
需要使用parse模块
'''
if __name__ == '__main__':
    url = "http://www.baidu.com/s?"
    wd = input("input your keyword: ")

    # 想要使用data,需要使用字典结构
    qs = {
        "wd": wd
    }
    # 转换url编码
    qs = parse.urlencode(qs)

    fullurl = url + qs
    print(fullurl)
    # 不能用可读的中文字符读取
    rsp = request.urlopen(fullurl)

    html = rsp.read()
    html = html.decode()
    print(html)
