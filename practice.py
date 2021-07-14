import requests
from bs4 import BeautifulSoup

website = requests.get('https://quotes.toscrape.com/')
# print(website) # It returns a response object
# print(website.text) # It will return the whole HTML page of the website

# Declaring BeautifulSoup Object
soup = BeautifulSoup(website.text, 'html.parser')

# Let's first try to get the title of the website
title = soup.find('title')
print(title.text)

# Extracting element based on tag
link = soup.find('a') # will return the first <a> tag
print(link)

# Extracting element based on class name
quote = soup.find(class_ = 'text') # will return the first tag having the class 'text'
print(quote.text) 