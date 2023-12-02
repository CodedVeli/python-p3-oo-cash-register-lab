#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0):
        self.total = total
        self.discount = discount
        self.items = []   
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        for i in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * self.discount / 100
            return "After the discount, the total comes to $%d." % self.total
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount



               
  
