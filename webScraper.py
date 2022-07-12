import requests
from bs4 import BeautifulSoup

class Webscrape:
    def __init__(self):
        pass
    def priceBitcoin(self):

        url = "https://coinmarketcap.com/currencies/bitcoin/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        self.price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
        return self.price
    def typeBitcoin(self):
        url = "https://coinmarketcap.com/currencies/bitcoin/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
        return coin

    def trendIndicatorBitcoin(self):
        url = "https://coinmarketcap.com/currencies/bitcoin/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span', {'class': "icon-Caret-down"})
        return trendIndicator
    def trendNumberBitcoin(self):
        url = "https://coinmarketcap.com/currencies/bitcoin/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text
        return trendNumber
    def sourceBitcoin(self):
        url = "https://coinmarketcap.com/currencies/bitcoin/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
        return source

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

    def priceEterium(self):

        url = "https://coinmarketcap.com/currencies/ethereum/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        self.price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
        return self.price
    def typeEterium(self):
        url = "https://coinmarketcap.com/currencies/ethereum/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
        return coin

    def trendIndicatorEterium(self):
        url = "https://coinmarketcap.com/currencies/ethereum/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span', {'class': "icon-Caret-down"})
        return trendIndicator
    def trendNumberEterium(self):
        url = "https://coinmarketcap.com/currencies/ethereum/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text
        return trendNumber
    def sourceEterium(self):
        url = "https://coinmarketcap.com/currencies/ethereum/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
        return source
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

    def priceDodgecoin(self):

        url = "https://coinmarketcap.com/currencies/dogecoin/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        self.price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
        return self.price
    def typeDodgecoin(self):
        url = "https://coinmarketcap.com/currencies/dogecoin/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
        return coin

    def trendIndicatorDodgecoin(self):
        url = "https://coinmarketcap.com/currencies/dogecoin/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span', {'class': "icon-Caret-down"})
        return trendIndicator
    def trendNumberDodgecoin(self):
        url = "https://coinmarketcap.com/currencies/dogecoin/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text
        return trendNumber
    def sourceDodgecoin(self):
        url = "https://coinmarketcap.com/currencies/dogecoin/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
        return source
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

    def priceTether(self):

        url = "https://coinmarketcap.com/currencies/tether/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        self.price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
        return self.price
    def typeTether(self):
        url = "https://coinmarketcap.com/currencies/tether/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
        return coin

    def trendIndicatorTether(self):
        url = "https://coinmarketcap.com/currencies/tether/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span', {'class': "icon-Caret-down"})
        return trendIndicator
    def trendNumberTether(self):
        url = "https://coinmarketcap.com/currencies/tether/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text
        return trendNumber
    def sourceTether(self):
        url = "https://coinmarketcap.com/currencies/tether/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
        return source
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

    def priceCatGirl(self):

        url = "https://coinmarketcap.com/currencies/catgirl/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        self.price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
        return self.price
    def typeCatGirl(self):
        url = "https://coinmarketcap.com/currencies/catgirl/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
        return coin

    def trendIndicatorCatGirl(self):
        url = "https://coinmarketcap.com/currencies/catgirl/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span', {'class': "icon-Caret-down"})
        return trendIndicator
    def trendNumberCatGirl(self):
        url = "https://coinmarketcap.com/currencies/catgirl/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text
        return trendNumber
    def sourceCatGirl(self):
        url = "https://coinmarketcap.com/currencies/catgirl/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
        return source
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

    def priceCelsius(self):

        url = "https://coinmarketcap.com/currencies/celsius/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        self.price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
        return self.price
    def typeCelsius(self):
        url = "https://coinmarketcap.com/currencies/celsius/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
        return coin

    def trendIndicatorCelsius(self):
        url = "https://coinmarketcap.com/currencies/celsius/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span', {'class': "icon-Caret-down"})
        return trendIndicator
    def trendNumberCelsius(self):
        url = "https://coinmarketcap.com/currencies/celsius/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text
        return trendNumber
    def sourceCelsius(self):
        url = "https://coinmarketcap.com/currencies/celsius/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
        return source
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

    def priceBitbook(self):

        url = "https://coinmarketcap.com/currencies/bitbook/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        self.price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
        return self.price
    def typeBitbook(self):
        url = "https://coinmarketcap.com/currencies/bitbook/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
        return coin

    def trendIndicatorBitbook(self):
        url = "https://coinmarketcap.com/currencies/bitbook/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span', {'class': "icon-Caret-down"})
        return trendIndicator
    def trendNumberBitbook(self):
        url = "https://coinmarketcap.com/currencies/bitbook/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text
        return trendNumber
    def sourceBitbook(self):
        url = "https://coinmarketcap.com/currencies/bitbook/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
        return source
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

    def priceSandbox(self):

        url = "https://coinmarketcap.com/currencies/the-sandbox/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        self.price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
        return self.price
    def typeSandbox(self):
        url = "https://coinmarketcap.com/currencies/the-sandbox/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
        return coin

    def trendIndicatorSandbox(self):
        url = "https://coinmarketcap.com/currencies/the-sandbox/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span', {'class': "icon-Caret-down"})
        return trendIndicator
    def trendNumberSandbox(self):
        url = "https://coinmarketcap.com/currencies/the-sandbox/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text
        return trendNumber
    def sourceSandbox(self):
        url = "https://coinmarketcap.com/currencies/the-sandbox/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
        return source
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

    def priceM7v2(self):

        url = "https://coinmarketcap.com/currencies/m7v2/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        self.price = soup.find_all('div', {'class': "priceValue"})[0].find('span').text
        return self.price
    def typeM7v2(self):
        url = "https://coinmarketcap.com/currencies/m7v2/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        coin = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].text
        return coin

    def trendIndicatorM7v2(self):
        url = "https://coinmarketcap.com/currencies/m7v2/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendIndicator = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span', {'class': "icon-Caret-down"})
        return trendIndicator
    def trendNumberM7v2(self):
        url = "https://coinmarketcap.com/currencies/m7v2/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        trendNumber = soup.find_all('div', {'class': "sc-16r8icm-0 kjciSH priceTitle"})[0].find_all('span')[1].text
        return trendNumber
    def sourceM7v2(self):
        url = "https://coinmarketcap.com/currencies/m7v2/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        source = soup.find_all('div', {'class': "sc-16r8icm-0 gpRPnR nameHeader"})[0].find('img')['src']
        return source
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

