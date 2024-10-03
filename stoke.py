# Import libraries
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# Create Funcion to stock data 

def stokeCrypto(name):

    # Funcion to standardize name
    def wordopt(name):
        return name.lower().replace(' ','-')
    name = wordopt(name)

    # Getting data from URL 
    headers = {'Headers - Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0'}
    url = f'https://www.binance.com/en/price/{name}'
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')

    # 
    if soup.find('div',{'class':'css-1267ixm'}).find('div',{'class':'css-4j2do9'}):
        change = soup.find('div',{'class':'css-1267ixm'}).find('div',{'class':'css-4j2do9'}).text.replace('%','')
    elif soup.find('div',{'class':'css-1267ixm'}).find('div',{'class':'css-12i542z'}):
        change = soup.find('div',{'class':'css-1267ixm'}).find('div',{'class':'css-12i542z'}).text.replace('+','').replace('%','')
    else :
        change = None
    
    if change == "<0.01":
        change = 0

    stoke = {
        'name'  : name,
        'time'  : datetime.now().strftime("%Y-%m-%d %H:%M"),
        'price' : float(soup.find('div',{'class':'css-1267ixm'}).find('div',{'class':'css-1bwgsh3'}).text.replace('$','').replace('USD','').replace(',','')),
        'change': float(change)
    }
    return stoke