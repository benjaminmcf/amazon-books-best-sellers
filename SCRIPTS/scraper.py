from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime,date

country_dict = {
    'AUS': 'https://www.amazon.com.au/gp/bestsellers/books/ref=zg_bs_pg_1_books?ie=UTF8&pg=1'
}

url = country_dict['AUS']
rank_list = []
author_list = []
title_list = []
date_list = []
time_list = []


response = requests.get(url)
print(f'Response status = {response.status_code}')
    
# Check if the request was successful (status code 200)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    div_element = soup.findAll('div',id="gridItemRoot")
    for item in div_element:
        rank = item.find('span').text.split('#')[1]
        author = item.find('div',class_="a-row a-size-small").text
        x = item.find_all('a',class_="a-link-normal")
        title = x[1].find('span').text      

        rank_list.append(rank)
        author_list.append(author)
        title_list.append(title)
        date_list.append(datetime.now().strftime("%d/%m/%Y"))
        time_list.append(datetime.now().strftime("%H:%M:%S"))

    
    df_top_selling = pd.DataFrame({"Rank":rank_list,"author":author_list,"book title":title_list,"date":date_list,"time":time_list})
    df_top_selling.to_csv(f'../DATA/AUS/aus_top_selling_books_{datetime.now().strftime(("%d_%m_%Y"))}_{datetime.now().strftime("%H_%M_%S")}.csv',index=False)

else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)