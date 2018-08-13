import urllib


# if __name__ == '__main__':
#     url = "https://jobs.zhaopin.com/390261416251663.htm"
#
#     rsp = urllib.request.urlopen(url)
#
#     print(type(rsp))
#     print(rsp)
#
#     # html = rsp.read()
#     # print(html)

if __name__ == '__main__':
    url = "https://jobs.zhaopin.com/390261416251663.htm"

    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("URL: {0}".format(rsp.geturl()))
    print("MetaInfo: {0}".format(rsp.info()))
    print("Code: {0}".format(rsp.getcode()))
