import requests
from bs4 import BeautifulSoup
import re
url = 'https://finance.yahoo.com/trending-tickers'
page = requests.get(url)
symbol=[]
name=[]
soup = BeautifulSoup(page.text, 'html.parser')
tables = soup.find('tbody')
rows = tables.find_all('tr')
for col in rows:
    column = col.find_all('td')
    symbol.append(column[0].text.strip())
    name.append(column[1].text.strip())
file  = open('tickers.txt','w')
for i in range(4,10):
    file.write(symbol[i]+"--->"+name[i]+"\n")

print('Finish......')
file.close()








