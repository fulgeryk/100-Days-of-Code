from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/show")
web_page = response.text

article_text = []
article_links = []

soup = BeautifulSoup(web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

for article_tag in articles:
    article_text.append(article_tag.getText())

article_link = soup.find_all(name="span", class_="sitestr")

for article in article_link:
    article_links.append(article.getText())

article_upvote = soup.find_all(name="span", class_="score")
article_points =[score.getText() for score in article_upvote]


only_points = [int(x.split()[0]) for x in article_points]

# y = 0
# for x in only_points:
#     if x > y:
#         y = x

y = max(only_points)
index_list = only_points.index(y)
print(article_text[index_list])
print(article_links[index_list])
