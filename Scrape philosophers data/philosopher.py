import requests
from bs4 import BeautifulSoup
import csv

# We are scrapping the data of first philosopher on:
# https://www.britannica.com/topic/list-of-philosophers-2027173#ref327483
# then we will scrape the data of rest
website = requests.get('https://www.britannica.com/biography/Mortimer-J-Adler')

soup = BeautifulSoup(website.text, 'html.parser')

name = soup.select_one('h1').text
about = soup.select_one('.topic-identifier').text
summary = soup.select_one('.topic-paragraph').text
print(summary)
