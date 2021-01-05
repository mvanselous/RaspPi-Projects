from bs4 import BeautifulSoup
import requests

#Webscraping function I will use to collect historical ticker data from yahoo finance. 

def find_ticker_price(ticker):
    AdjClose_Record = []
    High_Record = []
    Low_Record = []
    
    url = ''.join(('https://finance.yahoo.com/quote/',ticker,'/history?p=',ticker))
    page = requests.get(url).text
    soup = BeautifulSoup(page,'lxml')
    all_cols = soup.find_all('tr',class_="BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)",limit=7)
    
    for col in range(0,7):
        data = all_cols[col].find_all('td', class_="Py(10px) Pstart(10px)")
        AdjClose_Record.append(float(data[4].text.replace(',','')))
        High_Record.append(float(data[1].text.replace(',','')))
        Low_Record.append(float(data[2].text.replace(',','')))
    AdjClose_Record.reverse()
    High_Record.reverse()
    Low_Record.reverse()
    
    #print(f'The current price of {ticker} is {adj_close}')
    return AdjClose_Record,High_Record,Low_Record

data = find_ticker_price('BTC-USD')

print(f'AdjClose Data: \n',data[0],'\n')
print(f'High Data: \n',data[1],'\n')
print(f'Low Data: \n',data[2],'\n')
    