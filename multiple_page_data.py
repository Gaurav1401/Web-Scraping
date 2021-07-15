# Extracting data from multiple pages

import requests
from bs4 import BeautifulSoup
page = 1
next_button = True
while next_button: # If next button exists
    website = requests.get('https://quotes.toscrape.com/page/'+str(page))

    # Declaring BeautifulSoup Object
    soup = BeautifulSoup(website.text, 'html.parser')

    # From the website we can understand that if a page has next button available
    # only then we can move to another page

    # On the page, we can clearly see that class next contains the link of next page

    next_button = soup.select_one('.next > a') # selecting a tag from every class next

    quotes = soup.select('.quote')

    for quote in quotes:
        text = quote.select_one('.text')
        print(text.text)
        author = quote.select_one('.author')
        print(author.text)
        tags = quote.select('.tag')
        for tag in tags:
            print(tag.text)
        print('\n ***************************** \n')
    print(page)
    page+=1