# -*- coding: utf-8 -*-

import bs4 as bs
import re
import requests
import pandas as pd
import numpy
import lxml.etree
import lxml.html

url = "http://www.jegkorongblog.hu/"
def get_article_links():
    response = requests.get(url)
    soup = bs.BeautifulSoup(response.text, "lxml")
    pattern = url + r'\d{4}\/\d{2}\/\d{2}\/\w+(-\w*)*\/#post-\d{6}'
    a_tags = soup.find_all(href=re.compile(pattern))
    article_links = [item['href'] for item in a_tags]
    unique_article_links = list(set(article_links))
    return unique_article_links

def get_article_text():
    articles = get_article_links()
    titles = []
    texts = []
    for article in articles:
        response = requests.get(article)
        soup = bs.BeautifulSoup(response.text, "lxml")
        title = soup.h1.find(text=True, recursive=False)
        titles.append(title)
        p_tags = soup.find('div', class_='entrytext').find_all('p')
        text = [p.text for p in p_tags]
        article_text = ' '.join(text)
        texts.append(article_text)
    icehockey_articles = {'title': titles, 'link': articles, 'text': texts}
    df = pd.DataFrame(icehockey_articles, columns = icehockey_articles.keys())
    df.to_csv('jegkorongblog.csv') 
    return df

print(get_article_text().head())