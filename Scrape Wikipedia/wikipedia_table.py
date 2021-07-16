import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')

soup = BeautifulSoup(website.text, 'html.parser')

first_table = soup.select_one('.wikitable')
table_rows = first_table.select('tr')[2:]

for row in table_rows[:3]:
    table_data = row.select('td')
    country = table_data[0].find('a').text
    print(country)