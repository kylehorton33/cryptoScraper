#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import libraries
import requests #pull data from url
from bs4 import BeautifulSoup as bs4 #parse HTML
import pandas as pd #arrange in dataframe
from re import sub #regular expression substitution


# In[ ]:


#initialize arrays
ranks = []
ticker = []
names = []
market_cap = []
price_usd = []
vol_24hr = []
circ_supply = []
change_24hr = []
names = []


# In[ ]:


#pull html data from url
url = 'https://coinmarketcap.com/'
page = requests.get(url)
soup = bs4(page.text, 'html.parser')


# In[ ]:


#fill arrays with top 100 crypto
block = []
new_block = []
for i in soup.findAll('tr'):
    block.append(i.getText())
for j in range(len(block)):
    new_block.append(block[j].split('\n'))

for k in range(1,len(block)):
    while True:
        try:
            new_block[k].remove('')
        except ValueError:
            break
    while True:
        try:
            new_block[k].remove('*')
        except ValueError:
            break
    ranks.append(new_block[k][0])
    ticker.append(new_block[k][1])
    names.append(new_block[k][2])
    market_cap.append(new_block[k][3])
    price_usd.append(new_block[k][4])
    vol_24hr.append(new_block[k][5])
    circ_supply.append(new_block[k][6])
    change_24hr.append(new_block[k][8])


# In[ ]:


#create dictionary from arrays
data = {"Rank" : ranks, "Ticker" : ticker, "Name" : names, "Market Cap" : market_cap, "Price (USD)" : price_usd, "Volume (24h)" : vol_24hr, "Circulating Supply" : circ_supply, "Change (24h)" : change_24hr}
df = pd.DataFrame(data = data) #create dataframe from dictionary
df2 = df.set_index("Ticker", drop = False) #reset index to 3-letter ticker code


# In[ ]:


#example calculator for ratios
btc_price = df2.loc["BTC","Price (USD)"]
eth_price = df2.loc["ETH","Price (USD)"]
btc = float(sub(r'[^\d.]','', btc_price))
eth = float(sub(r'[^\d.]','', eth_price))
eth/btc


# In[ ]:




