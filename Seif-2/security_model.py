# מחלקת האב Security
class Security:
    def __init__(self, name, symbol, current_price):
        self.name = name
        self.symbol = symbol
        self.current_price = current_price

    def show_base_info(self):
        print(f"Security Name: {self.name}")
        print(f"Symbol: {self.symbol}")
        print(f"Current Price: {self.current_price}")

# ירושה ממחלקת האב - Stock
class Stock(Security):
    def __init__(self, name, symbol, current_price, dividend_yield):
        super().__init__(name, symbol, current_price)
        self.dividend_yield = dividend_yield

    def show_dividend_info(self):
        print(f"Dividend Yield: {self.dividend_yield}%")

# ירושה ממחלקת האב - Bond
class Bond(Security):
    def __init__(self, name, symbol, current_price, interest_rate):
        super().__init__(name, symbol, current_price)
        self.interest_rate = interest_rate

    def show_interest_info(self):
        print(f"Interest Rate: {self.interest_rate}%")

# ירושה ממחלקת האב - Option
class Option(Security):
    def __init__(self, name, symbol, current_price, expiration_date):
        super().__init__(name, symbol, current_price)
        self.expiration_date = expiration_date

    def show_expiration_info(self):
        print(f"Expiration Date: {self.expiration_date}")