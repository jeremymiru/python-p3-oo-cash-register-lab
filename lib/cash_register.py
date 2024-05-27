#!/usr/bin/env python3

class CashRegister:
  def __init__(self,thediscount=0):
    self.discount = thediscount
    self.total = 0
    self.items = []
    self.last_transaction = 0

    def add_item(self,title,price,quantity=1):
      self.items.append(title)
      self.total += price * quantity
      self.last_transaction = price * quantity

      def apply_discount(self):
        if self.discount == 0:
          print("There is no discount to apply.")
        else:
          self.total -= self.total * (self.discount / 100)
          print("After the discount, the total comes to ${:.2f}.".format(self.total))


          def void_last_transaction(self):
            self.total -= self.last_transaction
            self.last_transaction = 0
