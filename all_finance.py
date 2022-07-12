#01
import Numpy_Financial as npf

cfl = [-50000, 10000, 25000, 25000, 35000, 42000] 
cf2 = [-30000, 10000, 13000, 18000, 25000, 20000]

print("Option 1: ", npf.irr(cf1)) 
print("Option 2: ", npf.irr(cf2)) 

#02
import matplotlib.pyplot as plt

x = [2, 8, 42, 1]

plt.plot(x)

#03
import pandas as pd
prices = [42.8, 102.03, 240.38, 80.9] 
s = pd.Series(prices) 

#04
data = { 'date': •2021-06-10•, .2021-00- .2021-06-131, 'Prices.: [42.a, 102. 88.9] 
df = pd.DataFrame(data) 
print(df) 

#05
data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

#06
data = { 'date': •2021-06-10•, .2021-00- .2021-06-131, 'Prices.: [42.a, 102. 88.9] 
df = pd.DataFrame(data) 
print(a1) 

#07
data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%2 6P_500_companies') 
df = data[0] 
df = df[['Symbol', 'Security']] 
print(df) 

#08
df[df['Security'] == 'Apple']

#09
url_link = 
'https://finance.yahoo.com/quote/TSLA/profile' 
r = requests.get(url_link,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; win64; x64) 
AppleWebKit/537.36 (KHTML, like Gecko) 
Chrome/91.0.4472.124 Safari/537.36'1) 

#10
import pandas as pd 
import requests 

url_link = 'https://finance.yahoo.com/quote/TSLA/profile' 
r = requests.get(url_link,headers WUser-
Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
AppleWebKit/537.36 (KHTML, like Gecko) 
Chrome/91.0.4472.124 Safari/537.36'D 

data = pd.read_html(r.text) 
print(data[0]) 

#11
url_link 
= ghttps://finance.yahoo.com/quote/TSLA/analysis?p=TSLA' 
data = pd.read_html(r.text) 
print(data[0]) 

#12
data = data[data['Earnings Estimate'] == 'Avg. 
Estimate'] 
data.plot(kind='bar') 

#13
import yfinance as yf

import matplotlib.pyplot as plt
data = yf.Ticker("TSLA")

x = data.earnings
x.plot(kind="bar")

#14

import yfinance as yf

import matplotlib.pyplot as plt

data = yf.Ticker("TSLA")

x = x.(kind="bar")

#15


