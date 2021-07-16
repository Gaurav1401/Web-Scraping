import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')

soup = BeautifulSoup(website.text, 'html.parser')

first_table = soup.select_one('.wikitable')
table_rows = first_table.select('tr')[2:]

record = {} # Empty dictionary
csv_data = [['Country', 'Continent', 'Population', '%age of the world', 'Date', 'Source']]

for row in table_rows:
    table_data = row.select('td')
    country = table_data[0].find('a').text
    continent = table_data[1].find('a').text
    population = table_data[2].text
    percent = table_data[3].text
    date = table_data[4].find('span').text
    source = table_data[5].text.split('[')[0]
    csv_data.append([country, continent, population, percent, date, source])

print(csv_data)