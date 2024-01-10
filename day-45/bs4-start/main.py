from bs4 import BeautifulSoup
import requests
from pprint import pprint

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.find_next().get("href")
    article_links.append(link)
print(article_texts)
print(article_links)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)
print(max(article_upvotes))
max_index=article_upvotes.index(max(article_upvotes))
print(article_links[max_index])
print(article_texts[max_index])









# # import lxml
#
# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(1, soup.title)
# print(2, soup.title.string)
#
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name='p')
# print(3, all_anchor_tags)
# #
# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     tag.get"href")
# #
# heading = soup.find(name="h1", id="name")
# print(4, heading)
#
# class_is_heading = soup.find_all(class_="heading")
# print(5, class_is_heading)
#
# h3_heading = soup.find(name="h3", class_="heading")
# print(6, h3_heading)
#
# company_url = soup.select_one(selector="p a")
# print(7, company_url)
#
# name = soup.select_one(selector="#name")
# print(8, name)
#
# headings = soup.select(".heading")
# print(9, headings)