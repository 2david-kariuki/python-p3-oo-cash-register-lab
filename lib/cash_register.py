class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self._last_transaction_amount = 0
        self._last_transaction_items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self._last_transaction_amount = price * quantity
        self._last_transaction_items = [title] * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            # Cast total to int if it is whole number, else keep as float rounded to 2 decimals
            if self.total == int(self.total):
                self.total = int(self.total)
            else:
                self.total = round(self.total, 2)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Subtract the last transaction amount from total
        self.total -= self._last_transaction_amount
        # Remove the last transaction items from the items list
        for item in self._last_transaction_items:
            if item in self.items:
                self.items.remove(item)
        # Reset last transaction info
        self._last_transaction_amount = 0
        self._last_transaction_items = []

        # Ensure total doesn't go below 0
        if self.total < 0:
            self.total = 0
