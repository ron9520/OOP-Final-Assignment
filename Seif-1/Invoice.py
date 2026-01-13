class Invoice:
    def __init__(self, id, client_name, date, currency, amount):
        # אתחול תכונות
        self.id = id
        self.client_name = client_name
        self.date = date
        self.currency = currency
        self._amount = amount

    @property
    def amount(self):
        # קבלת סכום
        return self._amount

    @amount.setter
    def amount(self, value):
        # בדיקת תקינות סכום
        if value < 0:
            raise ValueError("Amount cannot be negative")
        self._amount = value

    def print_details(self):
        # הדפסת פרטי החשבונית
        print(f"Invoice ID: {self.id}")
        print(f"Client Name: {self.client_name}")
        print(f"Date: {self.date}")
        print(f"Currency: {self.currency}")
        print(f"Amount: {self.amount}")

    def apply_tax(self, tax_rate):
        # חישוב מס
        tax_amount = self.amount * tax_rate / 100
        self.amount += tax_amount
        print(f"Tax applied: {tax_amount} {self.currency}")