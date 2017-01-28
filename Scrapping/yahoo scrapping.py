# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import requests
import re
from bs4 import BeautifulSoup

base_url = "https://tw.news.yahoo.com"
url = "https://tw.news.yahoo.com/finance/archive/"
pages = range(1, 40)  # scrape for 40 pages, for each page with 25 news.
links = []
for page in pages:
    print(url + str(page) + ".html")
    print("===")
    yahoo_r = requests.get(url + str(page) + ".html")
    yahoo_soup = BeautifulSoup(yahoo_r.text, 'html.parser')
    finance = yahoo_soup.findAll('div', {'class': 'story'})
    for info in finance:
        link = ""
        try:
            link = info.findAll('a', href=True)[0]
            if link.get('href') != '#':
                links.append(base_url + link.get("href"))
                print(base_url + link.get("href"))
                print('===')
        except:
            link = None

print(len(links))
print(links)

title = ""
time = ""
content = ""
test = True
for link in links[0:]:
    news = requests.get(link)
    single_news = BeautifulSoup(news.text, 'html.parser')
    try:
        title = single_news.findAll('h1', {'class': 'headline'})
        time = single_news.findAll('abbr')[0].get('title')
        time = time.replace(':', '-')
        content = single_news.find_all('div', {'itemtype': 'https://schema.org/Article'})
        file_path = '{timestamp}.txt'.format(timestamp=time)
        with open(file_path, 'w') as textfile:
            print(title[0].text)
            textfile.write(title[0].text + '\n')
            textfile.write(time + '\n\n')
            try:
                for line in content[0].text.split('\n'):
                    if line.strip() != '':
                        textfile.write(line)
            except:
                print('error!')
            textfile.close()
    except:
        print(title)
        print(time)
        continue


