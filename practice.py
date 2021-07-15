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

quote = soup.find_all(class_ = 'quote')
# quote_text = quote.find(class_ = 'text')
# author = quote.find(class_ = 'author')

# Extracting all quotes and their respective authors
author_lst = []
for i in quote:
    author = i.find(class_='author')
    author_lst.append(author.text)

quote_lst = []
for i in quote:
    text = i.find(class_ = 'text')
    quote_lst.append(text.text)

# Storing records in dataframe
record = {}
record['Quote'] = quote_lst
record['Author'] = author_lst

import pandas as pd

# df = pd.DataFrame(record)
# print(df)

# Doing the same thing using CSS selectors

quotes = soup.select('.quote')

q_lst = []
a_lst = []
t_lst = []
all_tag = []
for quote in quotes:
    t_lst = []
    text = quote.select_one('.text')
    q_lst.append(text.text)
    author = quote.select_one('.author')
    a_lst.append(author.text)
    tags = quote.select('.tag')
    for tag in tags:
        t_lst.append(tag.text)
    all_tag.append(t_lst)

record = {}

record['Quote'] = q_lst
record['Author'] = a_lst
record['Tags'] = all_tag

scraped_data = pd.DataFrame(record)
print(scraped_data)