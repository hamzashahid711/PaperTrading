import requests
from bs4 import BeautifulSoup
class Webscrape:
    def priceTrackBitcoin(self):

        while True:
            url = "https://coinmarketcap.com/currencies/bitcoin/"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
            source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
            coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
            # if not down then list will be empty and it will have to be going up
            trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span', {'class': "icon-Caret-down"})
            trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text

    def priceTrackEthereum(self):

        while True:
            url = "https://coinmarketcap.com/currencies/ethereum/"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
            source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
            coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
            # if not down then list will be empty and it will have to be going up
            trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span', {'class': "icon-Caret-down"})
            trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text

    def priceTrackDodgecoin(self):

        while True:
            url = "https://coinmarketcap.com/currencies/dogecoin/"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
            source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
            coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
            # if not down then list will be empty and it will have to be going up
            trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span', {'class': "icon-Caret-down"})
            trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text

    def priceTrackTether(self):

        while True:
            url = "https://coinmarketcap.com/currencies/tether/"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
            source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
            coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
            # if not down then list will be empty and it will have to be going up
            trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span', {'class': "icon-Caret-down"})
            trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text

    def priceTrackCatGirl(self):

        while True:
            url = "https://coinmarketcap.com/currencies/catgirl/"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
            source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
            coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
            #if not down then list will be empty and it will have to be going up
            trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span',{'class': "icon-Caret-down"})
            trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text

    def priceTrackCelsius(self):

        while True:
            url = "https://coinmarketcap.com/currencies/celsius/"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
            source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
            coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
            #if not down then list will be empty and it will have to be going up
            trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span',{'class': "icon-Caret-down"})
            trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text

    def priceTrackBitbook(self):

        while True:
            url = "https://coinmarketcap.com/currencies/bitbook/"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
            source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
            coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
            #if not down then list will be empty and it will have to be going up
            trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span',{'class': "icon-Caret-down"})
            trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text

    def priceTrackSandbox(self):

        while True:
            url = "https://coinmarketcap.com/currencies/the-sandbox/"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
            source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
            coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
            #if not down then list will be empty and it will have to be going up
            trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span',{'class': "icon-Caret-down"})
            trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text

    def priceTrackM7v2(self):

        while True:
            url = "https://coinmarketcap.com/currencies/m7v2/"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
            source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
            coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
            #if not down then list will be empty and it will have to be going up
            trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span',{'class': "icon-Caret-down"})
            trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text
