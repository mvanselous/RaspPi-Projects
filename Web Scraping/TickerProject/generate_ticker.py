from bs4 import BeautifulSoup
import requests
import numpy as np

def find_ticker_data(ticker):
    close = []; high = []; low = []
    url = ''.join(('https://finance.yahoo.com/quote/',ticker,'/history?p=',ticker))
    page = requests.get(url).text
    soup = BeautifulSoup(page,'lxml')
    all_cols = soup.find_all('tr',class_="BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)",limit=15)
    #I set limit=15 incase of a prolonged bank holiday.
    #We want quick access to this data so that we can find the most recent
    #closing price.
    for col in range(0,7):
        data = all_cols[6-col].find_all('td', class_="Py(10px) Pstart(10px)")
        try:
            close.append(float(data[4].text.replace(',','')))
            high.append(float(data[1].text.replace(',','')))
            low.append(float(data[2].text.replace(',','')))
        except ValueError:
            print(data[4].text.replace(',',''))
            if col != 0:
                close.append(close[-1])
            else:
                idx = 0
                print('Bank Holiday Else Needed')
                while data[4].text.replace(',','') == '-':
                    print('While Used')
                    data = all_cols[7+idx].find_all('td', class_="Py(10px) Pstart(10px)")
                    idx +=1
                close.append(float(data[4].text.replace(',','')))
            high.append(close[-1])
            low.append(close[-1])
    return close,high,low

class Ticker:
    def __init__(self,ticker):
        self.close, self.high, self.low = find_ticker_data(ticker)
        self.max = max(self.close + self.high + self.low)
        self.min  = min(self.close + self.high + self.low)
        self.spread = self.max - self.min
        self.change = (self.close[6]-self.close[0])
        self.percent_change = self.change/self.close[0]*100
        
