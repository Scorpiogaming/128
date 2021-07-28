from selenium import webdriver 
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser=webdriver.Chrome('chromedriver')
browser.get(START_URL)
soup = BeautifulSoup(browser.page_source, "html.parser")
stars_table=soup.find('table')
temp_list=[]
table_rows=stars_table.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td ]
    temp_list.append(row)
stars_names=[]
distance=[]
mass=[]
radius=[]
for i in range(1,len(temp_list)):
    stars_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])
df2=pd.DataFrame(list(zip(stars_names,distance,mass,radius)),columns=['name','dis','ms','rd'])
df2.to_csv('stars.csv')