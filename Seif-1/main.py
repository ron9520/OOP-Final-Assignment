from Invoice import Invoice

# קבלת קלט מהמשתמש
id = input("Enter Invoice ID: ")
client_name = input("Enter Client Name: ")
date = input("Enter Date: ")
currency = input("Enter Currency: ")
amount = float(input("Enter Amount: "))

# יצירת אובייקט
invoice = Invoice(id, client_name, date, currency, amount)

# הדגמת שיטות
invoice.print_details()

# הדגמת מס
tax_rate = float(input("Enter Tax Rate (%): "))
invoice.apply_tax(tax_rate)
invoice.print_details()

# הדגמת ולידציה
try:
    invoice.amount = -100
except ValueError as e:
    print(f"Error: {e}")