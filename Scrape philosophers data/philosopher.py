import requests
from bs4 import BeautifulSoup
import csv

website = requests.get("https://www.britannica.com/topic/list-of-philosophers-2027173#ref327483")
soup = BeautifulSoup(website.text, "html.parser")

links = soup.select(".topic-list .md-crosslink")
for link in links[:8]: # Making requests only 8 times as if I make around 500 requests, I may get blocked by the website
    # We are scrapping the data of first philosopher on:
    # https://www.britannica.com/topic/list-of-philosophers-2027173#ref327483
    # then we will scrape the data of rest

    try: # if the website can't be scraped then
        website = requests.get(link.attrs["href"])

        soup = BeautifulSoup(website.text, 'html.parser')

        name = soup.select_one('h1').text
        about = soup.select_one('.topic-identifier').text
        summary = soup.select_one('.topic-paragraph').text
        try:
            image_src = soup.select_one('.fact-box-picture img').attrs['src'] # extracting attribute from a tag
        except AttributeError as error:
            image_src = None
        birth_date = soup.find(attrs={"data-label" : "born"}).find('dd').get_text(separator = '|').split('|')[0]
        death_date = soup.find(attrs={"data-label" : "died"}).find('dd').get_text(separator = '|').split('|')[0]

        try: # If the website has no information of subjects for a particular author
            subjects_of_study = soup.find(attrs={"data-label" : "subjects of study"}).select_one('ul')
            subjects_items = subjects_of_study.select('li')
            subjects = ""
            for items in subjects_items:
                subjects += items.text.strip() + ', '
        except AttributeError as error:
            subjects = None
        print(f"{name}\n {about}\n {summary}\n{image_src}\n{birth_date}\n{death_date}\n{subjects}")
    except:
        print("Something Went wrong")