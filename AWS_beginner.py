import requests
from lxml import etree


def get_subpages(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    link = selector.xpath('//*[@id="post-content"]/div[1]//p[1]/text()')
    question = ' '.join(link).strip()
    choiceA = selector.xpath('//*[@id="post-content"]/div[1]/p[2]//text()')
    choiceA = " ".join(choiceA).strip()
    choices = selector.xpath('//*[@id="post-content"]/div[1]/p[position() > 2]//text()')
    choices = " ".join(choices).strip().split("\n")
    choices.insert(0,choiceA)
    answers = selector.xpath('//*[@id="post-content"]//p[@class="rightAnswer"]/text()')
    answers = " ".join(answers).strip().strip("\n")
    explanation = selector.xpath('//*[@id="post-content"]/div[1]/blockquote//text()')
    explanation = " ".join(explanation).strip()
    try:
        with open("C:\\Users\\songjie\\Desktop\\AWS_beginner.txt", "a") as code:
            code.write(question + '\n')
            for x in choices:
                code.write(x + "\n")
            code.write("answers:" + answers + '\n')
            code.write(explanation + '\n')
            code.write('\n')

    except:
        print(question)


if __name__ == '__main__':
    page = 1
    counter = 0
    list = []
    while page < 53:
        url = 'https://www.briefmenow.org/amazon/category/exam-aws-saa-update-july-14th-2017/page/%s/'%(page)
        html = requests.get(url)
        selector = etree.HTML(html.text)
        subpages = selector.xpath('//article/header/h2/a//@href')
        for u in subpages:
            get_subpages(u)
            counter += 1
            print(counter)
        page += 1
