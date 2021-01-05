from bs4 import BeautifulSoup
import requests
from sense_hat import SenseHat

sense = SenseHat()

def find_crypto_price(coin):
    coin_url = ''.join(('https://coinmarketcap.com/currencies/', coin, '/markets/'))
    coin_page = requests.get(coin_url).text
    soup = BeautifulSoup(coin_page,'lxml')
    result = soup.find('div',class_="priceValue___11gHJ")
    result = result.text
    print(f'The current price of {coin} is {result}')
    return result
     
coin_list = ('bitcoin','ethereum','xrp','litecoin','bitcoin-cash')

results = []

for coin in coin_list:
    price = find_crypto_price(coin)
    results.append((coin,price))

for coin in results:
    sense.show_message(f'{coin[0]}: {coin[1]}')

    




