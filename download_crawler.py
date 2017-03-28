import requests
import re

html = requests.get('http://www.chinatorch.gov.cn/gxjsqyrdw/tree/tree-alls.htm')
main_html = 'http://www.chinatorch.gov.cn/gaoqi/rdba/'
use_link = re.findall("/gaoqi/rdba/(.......)", html.text)
link = re.findall("/gaoqi/rdba(.*?)',", html.text)
lis = []

for x in range(0, len(link)):
    s = main_html + link[x]
    lis.append(s)

for z in range(0, len(lis)):
    html1 = requests.get(lis[z])
    link1 = re.findall('href="(.*?).doc"',html1.text)#link1 gets the url before '.doc'
    filename = re.findall('">([\u4E00,-\u9fa5]+).doc',html1.text)
    print(filename)
    final_url = []
    for i in range(0, len(link1)):
        x = main_html + use_link[z] + link1[i] + '.doc'
        final_url.append(x)
        print(len(final_url))

    for j in range(len(final_url)):
        download_file = requests.get(final_url[j])
        print(filename)
        if (filename == []):
            continue
        with open("C:\\Users\\songjie\\Desktop\\qwer\\%s.doc"%filename[0], "wb") as code:
            code.write(download_file.content)

