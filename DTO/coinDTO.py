class CoinDTO:
    def __init__(self, price, type, trendIndicator, trendNumber, image):
        self.price = price
        self.type = type
        self.trendIndicator = trendIndicator
        self.trendNumber = trendNumber
        self.image = image


class Coin:
    def __init__(self, id, cost, type):
        self.id = id
        self.cost = cost
        self.type = type

