import requests
from bs4 import BeautifulSoup

def priceTrack():

    while True:
        url = "https://coinmarketcap.com/currencies/bitcoin/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
        print((price))
        exit(0)


priceTrack()

