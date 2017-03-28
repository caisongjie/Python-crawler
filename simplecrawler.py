import requests
from lxml import etree

url = 'http://www.chinatorch.gov.cn/gaoqi/rdba/201604/194f38fc052a4299905324663536a6a3.shtml'
html = requests.get(url)
selector = etree.HTML(html.text)
link = selector.xpath('//*[@id="allStyleDIV"]/p[5]/span[1]/a//@href')
print(link)
a = url.split('/')
print(a)
print('/'.join(a))
a[-1] = link[0]
b = '/'.join(a)
html1 = requests.get(b)
with open("C:\\Users\\songjie\\Desktop\\info.doc", "wb") as code:
    code.write(html1.content)
