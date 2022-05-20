from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, WebDriverException
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://general.bajajallianz.com/BagicNxt/hm/hmSearchExternalHosp.do")
driver.implicitly_wait(10)

def obj_to_text(obj):
    return obj.text

def to_upper(string):
  return string.upper()

dct = {'col2' : [],
       'col3' : [],
       'col4' : [],
       'col5' : [],
       'col6' : [],
       'col7' : [],
       'col8' : []}

states = ['Andhra Pradesh','Andaman and nicobar','Assam','Bihar','chandigarh','Chattisgarh','Chhattisgarh',
'delhi','dadra and nagar haveli','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand',
'Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya',
'Mizoram','Nagaland','Odisha, Orissa','pondicherry','Punjab','Rajasthan','secunderabad','Sikkim','Tamil Nadu',
'Telangana','Tripura','Uttar Pradesh','Uttarakhand','UTTARANCHAL','West Bengal']
states = list(map(to_upper, states))

for state in states:
    select = Select(driver.find_element(By.XPATH, '//*[@id="p_search_criteria.stringval1"]'))
    select.select_by_visible_text(f'{state}')
    driver.find_element(By.XPATH, '//*[@id="search"]').click()
    num_rows = len(driver.find_elements(By.XPATH, '//*[@id="result"]'))
    if num_rows > 0:
        while True:
            try:
                for i in range(2,9):
                    text = driver.find_elements(By.XPATH, f'//*[@id="result"]/td[{i}]')
                    text = list(map(obj_to_text, text))
                    dct['col'+str(i)] += text 
                driver.find_element(By.XPATH, '/html/body/form/div/div/div[2]/div[8]/div/div/a[2]').click()

            except (TimeoutException, WebDriverException) as e:
                break
    else:
        continue

cols = ['Hospital Name', 'Hospital Address', 'City Name', 'Pin Code', 'State', 'Hospital Type', 'Contact Number']
df = pd.DataFrame(dct)
df.columns = cols
df.to_csv('bajajallianz.csv')
# print(dct)