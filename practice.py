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