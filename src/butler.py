import requests
import math

class Butler():
    def __init__(self, email, password):
        self.login(email, password)
        self.getBalances()
        self.isNextBuy = True
        self.UPWARD_TREND_THRESH = 2.25
        self.DIP_THRESH = 2.25
        self.PROFIT_THRESH = 1.25
        self.STOP_LOSS_THRESH = -2.00
        self.lastOpPrice = 100.00

        # need to get current owned quantity
        self.quantity = 0
    
    def login(self, email, password):
        api = "https://trade-service.wealthsimple.com/auth/login"
        content = {"Content-Type": "application/json"}
        data = {"email": email, "password": password}
        request = requests.post(url = api, json = data, headers = content)

        if "\"error\":\"Not authorized\"" in request.text:
            error("Authentication failed")
        else:
            headers = request.headers
            self.accessToken = headers["X-Access-Token"]
            self.refreshToken = headers["X-Refresh-Token"]
            self.header = {"Content-Type": "application/json", "Authorization": self.accessToken}
    
    def attemptToMakeTrade(self):
        currentPrice = self.getMarketPrice()
        percentageDiff = (currentPrice - self.lastOpPrice) / self.lastOpPrice * 100

        if self.isNextBuy:
            attemptBuy(percentageDiff)
        else:
            attemptSell(percentageDiff)
    
    def attemptBuy(self, percentageDiff):
        if percentageDiff >= self.UPWARD_TREND_THRESH or percentageDiff <= self.DIP_THRESH:
            self.lastOpPrice = placeBuyOrder()
            self.isNextBuy = False
    
    def attemptSell(self, percentageDiff):
        if percentageDiff >= UPWARD_TREND_THRESH OR percentageDiff <= self.DIP_THRESH:
            self.lastOpPrice = placeSellOrder()
            self.isNextBuy = True

    # sends a GET request to the API for the account's balances
    def getBalances(self):
        api = "https://trade-service.wealthsimple.com/account/list"
        request = requests.get(url = api, headers = self.header)
        jsonResponse = request.json()
        self.balance = float(jsonResponse.items()["current_balance"])
    
    # sends a GET request to the API for the current price of what we're trading
    def getMarketPrice(self):
        # some ticker here..
        api = "https://trade-service.wealthsimple.com/securities?query="
    
    # 1) calculate the amount to sell (based on some threshold)
    #     i.e., 50% of total balance
    #     i.e., send a POST request to the API to do a sell operation
    def placeBuyOrder(self):
        api = "https://trade-service.wealthsimple.com/orders"

        # figure out how to get price of security
        price = 5.00
        percent = 0.5

        quantity = math.floor(math.floor(self.balance * percent)  / price)

        # figure out how to get security ID, this is $APPL
        securityID = "sec-s-76a7155242e8477880cbb43269235cb6"
        
        # need to figure out how to retrieve the top growing stocks to analyze

        data = {
            "security_id": securityID,
            "limit_price": price,
            "quantity": quantity,
            "order_type": "buy_quantity",
            "order_sub_type": "limit",
            "time_in_force": "day"
        }

        request = requests.post(url = api, json = data, headers = self.header)

        filledAt = request.json().items()["filled_at"]
        self.getBalances()

        self.quantity = self.quantity + quantity
        
        # returns price at operation execution
        filledAt
    
    # send a POST request to the API to do a sell operation
    def placeSellOrder(self):
        api = "https://trade-service.wealthsimple.com/orders"

        # figure out how to get price of security
        price = 5.00

        # figure out how to get security ID, this is $APPL
        securityID = "sec-s-76a7155242e8477880cbb43269235cb6"

        data = {
            "security_id": securityID,
            "limit_price": price,
            "quantity": self.quantity, # just sell everything
            "order_type": "sell_quantity",
            "order_sub_type": "limit",
            "time_in_force": "day"
        }

        request = requests.post(url = api, json = data, headers = self.header)

        filledAt = request.json().items()["filled_at"]
        self.getBalances()
        
        # return price at operation execution
        filledAt
    
    # logger to show the bot's actions
    def log(self, type, message):
        print("[", type, "]", message)
    
    # throws errors and quits
    def error(self, message)
        self.log("ERROR", message)
        quit()
