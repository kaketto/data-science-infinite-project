import bs4 as bs
import requests as requests
import pandas as pd
import re

response = requests.get("http://finlandtoday.fi/feed")
print(response.status_code)
soup = bs.BeautifulSoup(response.text, "xml")
items = soup.find_all('item')

titles = []
links = []
dates = []
creators = []
categories = []
descriptions = []

for item in items:
    titles.append(item.title.text)
    links.append(item.link.text)
    dates.append(item.pubDate.text)
    creators.append(item.creator.text)
    article_categories = [child.text for child in item.children if child.name == "category"] 
    categories.append(', '.join(article_categories))
    description_p = "".join([re.split('<.?p>', child.string)[1] for child in item.children if child.name == "description"])
    descriptions.append(description_p)

news = {'title': titles, 'link': links, 'publication date': dates, 'author': creators, 'categories': categories, 'description': descriptions}
df = pd.DataFrame(news, columns = news.keys())
df.to_csv('rss2.csv')
print(df.head())