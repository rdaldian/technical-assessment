# Web Scraping or Crowling Using Beautiful Soup

# Importing the Libraries
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# Specifying the web address that we want to scrap
url_source = 'http://kompas.com/'

# Grabbing the page
uClient = uReq(url_source)
page_html = uClient.read()
uClient.close()

# HTML Parsing
page_soup = soup(page_html, "html.parser")

# Grabbing all the Most Popular News in each day
containers = page_soup.findAll("div", {"class":"most__list"})

filename = "popular_news.csv"
f = open(filename, "w", encoding = "utf-8")

headers = "news_title, total_read\n"

f.write(headers)

for container in containers:
    title_container = container.findAll("div", {"class":"most__title"})
    news_title = title_container[0].text

    read_container = container.findAll("div", {"class":"most__read"})
    total_read = read_container[0].text.replace("Dibaca", "")

    print("news_title: " + news_title)
    print("total_read: " + total_read)

    f.write(news_title.replace(",", " ") + "," + total_read + "\n")

f.close()