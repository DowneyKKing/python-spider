# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_html(url):
    # 伪装成浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    resp = requests.get(url, headers=headers).text
    return resp


def all_pages():
    all_urls = []
    for i in range(0, 490, 20):
        url = 'https://movie.douban.com/subject/26100958/comments?start=' \
              + str(i) + \
              '&limit=20&sort=new_score&status=P'
        all_urls.append(url)
    return all_urls


def html_operate():
    for url in all_pages():
        soup = BeautifulSoup(get_html(url), 'lxml')
        get_comment = soup.find_all('span', class_='short')
        comments = [a.get_text() for a in get_comment]
        for comment in comments:
            comment = str(comment) + '\n'
            f.writelines(comment + '————————————' + '\n')


filename = '复联4评论选取'
f = open(filename, 'w', encoding='utf-8')
html_operate()
f.close()
print('存储完成')
