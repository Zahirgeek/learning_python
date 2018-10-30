import requests
from lxml import etree

url = "http://qianmu.iguye.com/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D"
resp = requests.get(url)
selector = etree.HTML(resp.text)
links = selector.xpath("//div[@id='content']//td[2]/a/@href")

for link in links:
    if not link.startswith('http://qianmu.iguye.com/'):
        link = 'http://qianmu.iguye.com/%s'% link
    resp = requests.get(link)
    selector = etree.HTML(resp.text)
    data = {}
    data["name"] = selector.xpath('//div[@id="wikiContent"]/h1/text()')[0]
    print(data["name"])
    # 表格键值
    keys = selector.xpath('////div[@id="wikiContent"]/div[@class="infobox"]/table//td[1]/p/text()')
    cols = selector.xpath('//div[@id="wikiContent"]/div[@class="infobox"]/table//td[2]')

    # 将表格单行中有多个数据值合并
    values = [" ".join(col.xpath(".//text()")) for col in cols]

    if len(keys) != len(values):
        continue

    data.update(zip(keys, values))
    print(data)
