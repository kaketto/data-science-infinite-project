import bs4 as bs
import requests as requests
import pandas as pd

response = requests.get("http://finlandtoday.fi/feed")
print(response.status_code)
soup = bs.BeautifulSoup(response.text, "xml")
items = soup.find_all('item')
tags = []
news_list = []
i = 2

for item in items[0].children:
    if item.name:
        if item.name in tags:
            tags.append(item.name + str(i))
            i += 1
        else:
            tags.append(item.name)

for item in items:
    news = {}
    for child in item.children:
        if child.name:
            news[child.name] = child.text
    news_list.append(news)

df = pd.DataFrame(news_list, columns = tags)
del df['category2']
del df['category3']
del df['category4']
del df['category5']
del df['category6']
del df['comments7']
df.to_csv('rss.csv')
print(df.head())