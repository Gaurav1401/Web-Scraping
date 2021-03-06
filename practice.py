import requests
from bs4 import BeautifulSoup

website = requests.get('https://quotes.toscrape.com/')
# print(website) # It returns a response object
# print(website.text) # It will return the whole HTML page of the website

# Declaring BeautifulSoup Object
soup = BeautifulSoup(website.text, 'html.parser')

# Let's first try to get the title of the website
title = soup.find('title')
# print(title.text)

# Extracting element based on tag
link = soup.find('a') # will return the first <a> tag
# print(link)

# Extracting element based on class name
quote = soup.find(class_ = 'text') # will return the first tag having the class 'text'
# print(quote.text) 

# Extracting many elements at the same time
# Let's try to extract all the text of links available on website

links = soup.find_all('a') # all the a tags
#print(links) # It will return the whole tag in list format

# for i in links:
#     print(i.text) # Will retun all the texts which contains hyperlinks


quotes = soup.find_all(class_ = "text") # Getting all the quotes
# for i in quotes:
#     print(i.text)

# Using other attributes to extract elements
login_link = soup.find(href = '/login')
# print(login_link)

# Extracting elements from parent class

quote = soup.find(class_ = 'quote')
quote_text = quote.find(class_ = 'text')
author = quote.find(class_ = 'author')

# print(quote_text.text)
# print(author.text)

# Extracting elements using CSS selector

quote_text = soup.select_one(".text") # select the first element havign class = 'text'
# print(quote_text)

quotes = soup.select(".text") # select all the tags having class = 'text'
print(quotes)