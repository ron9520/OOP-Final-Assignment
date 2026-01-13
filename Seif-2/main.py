from security_model import Security, Stock, Bond, Option

# קבלת קלט מהמשתמש ליצירת אובייקט Stock
print("Enter details for Stock:")
stock_name = input("Name: ")
stock_symbol = input("Symbol: ")
stock_price = float(input("Current Price: "))
stock_dividend = float(input("Dividend Yield (%): "))

stock = Stock(stock_name, stock_symbol, stock_price, stock_dividend)

# קבלת קלט מהמשתמש ליצירת אובייקט Bond
print("\nEnter details for Bond:")
bond_name = input("Name: ")
bond_symbol = input("Symbol: ")
bond_price = float(input("Current Price: "))
bond_interest = float(input("Interest Rate (%): "))

bond = Bond(bond_name, bond_symbol, bond_price, bond_interest)

# קבלת קלט מהמשתמש ליצירת אובייקט Option
print("\nEnter details for Option:")
option_name = input("Name: ")
option_symbol = input("Symbol: ")
option_price = float(input("Current Price: "))
option_expiration = input("Expiration Date: ")

option = Option(option_name, option_symbol, option_price, option_expiration)

# הדפסת פרטי Stock
print("\nStock Details:")
stock.show_base_info()
stock.show_dividend_info()

# הדפסת פרטי Bond
print("\nBond Details:")
bond.show_base_info()
bond.show_interest_info()

# הדפסת פרטי Option
print("\nOption Details:")
option.show_base_info()
option.show_expiration_info()