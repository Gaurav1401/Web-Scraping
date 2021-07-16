import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')

soup = BeautifulSoup(website, 'html.parser')

