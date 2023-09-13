from abc import ABC, abstractmethod
from packaging import Packaging
from payable import Payable, PayType
from combine import Combinable

class DessertItem(Packaging):
    '''abstract class for dessert items'''
    def __init__(self, name="", tax_percent=7.25, packaging=None):
        self.name = name
        self.tax_percent = tax_percent
        self.packaging = packaging
      
    @abstractmethod
    def calculate_cost(self):
       pass
    
    def calculate_tax(self):
       return round(self.calculate_cost() * (self.tax_percent/100), 2)
    
    def __eq__(self, other_item):
       return self.calculate_cost() == other_item.calculate_cost()
    
    def __neq__(self, other_item):
       return self.calculate_cost() != other_item.calculate_cost()
    
    def __lt__(self, other_item):
       return self.calculate_cost() < other_item.calculate_cost()
    
    def __gt__(self, other_item):
       return self.calculate_cost() > other_item.calculate_cost()
    
    def __ge__(self, other_item):
       return self.calculate_cost() >= other_item.calculate_cost()
    
    def __le__(self, other_item):
       return self.calculate_cost() <= other_item.calculate_cost()

class Candy(DessertItem):
  def __init__(self, name="", tax_percent=7.25, weight=0.0, price_per_pound=0.0, packaging="Bag"):
    super().__init__(name, tax_percent, packaging)
    self.weight = weight
    self.price_per_pound = price_per_pound
  
  def calculate_cost(self):
     return round(self.weight * self.price_per_pound, 2)
  
  def can_combine(self, other: "Candy"):
     return isinstance(other, Candy) and self.name == other.name and self.price_per_pound == other.price_per_pound
  
  def combine(self, other: "Candy"):
     if self.can_combine(other):
        self.weight += other.weight

  
  def __str__(self):
     return f"{self.name} ({self.packaging})\n\t{str(self.weight) + 'lbs. @ $' + str(self.price_per_pound) +'/lb.:':45s} ${str(self.calculate_cost()):15s}[Tax: {self.calculate_tax()}]"

class Cookie(DessertItem):
  def __init__(self, name="", tax_percent=7.25, cookie_quantity=0, price_per_dozen=0.0, packaging="Box"):
    super().__init__(name, tax_percent, packaging)
    self.cookie_quantity = cookie_quantity
    self.price_per_dozen = price_per_dozen
  
  def calculate_cost(self):
     return round(self.cookie_quantity * (self.price_per_dozen / 12), 2)
  
  def can_combine(self, other: "Cookie"):
     return isinstance(other, Cookie) and self.name == other.name and self.price_per_dozen == other.price_per_dozen
  
  def combine(self, other: "Cookie"):
     if self.can_combine(other):
        self.cookie_quantity += other.cookie_quantity
  
  def __str__(self):
     return f"{self.name} ({self.packaging})\n\t{str(self.cookie_quantity) + ' cookies @ $' + str(self.price_per_dozen) + '/dozen:':45s} ${str(self.calculate_cost()):15s}[Tax: {self.calculate_tax()}]"

class IceCream(DessertItem):
    def __init__(self, name="", tax_percent=7.25, scoop_count=0, price_per_scoop=0.0, packaging="Bowl"):
      super().__init__(name, tax_percent, packaging)
      self.scoop_count = scoop_count
      self.price_per_scoop = price_per_scoop
    
    def calculate_cost(self):
       return round(self.scoop_count * self.price_per_scoop, 2)
    
    def __str__(self):
     return f"{self.name} Ice Cream ({self.packaging})\n\t{str(self.scoop_count) + ' scoops @ $' + str(self.price_per_scoop) + '/scoop:':45s} ${str(self.calculate_cost()):15s}[Tax: {self.calculate_tax()}]"

class Sundae(IceCream):
    def __init__(self, name="", tax_percent=7.25, scoop_count=0, price_per_scoop=0.0, topping_name="", topping_price=0.0, packaging="Boat"):
      super().__init__(name, tax_percent, scoop_count, price_per_scoop, packaging)
      self.topping_name = topping_name
      self.topping_price = topping_price

    def calculate_cost(self):
       return round(super().calculate_cost() + self.topping_price, 2)
    
    def __str__(self):
     return f"{self.name} Sundae ({self.packaging})\n\t{self.scoop_count} scoops of {self.name} ice cream @ ${self.price_per_scoop}/scoop\n\t{str(self.topping_name) + ' topping @ $' + str(self.topping_price) + ':':45s} ${str(self.calculate_cost()):15s}[Tax: {self.calculate_tax()}]"

class Order(Payable):
    def __init__(self, pay_type=PayType.CASH):
        self.order = []
        self.index = 0
        self.pay_type = pay_type
    
    def add(self, item):
        if isinstance(item, DessertItem):
            if (isinstance(item, Candy) or isinstance(item, Cookie)) and len(self.order) >= 1:
               combinable = False
               for dessert in self.order:
                  if item.can_combine(dessert):
                     dessert.combine(item)
                     combinable = True
                     break
               if not combinable:
                  self.order.append(item)
            else:
              self.order.append(item)
    
    def __len__(self):
        return len(self.order)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.order):
           item = self.order[self.index]
           self.index += 1
           return item
        else:
            print("There are no more items in the order")
    
    def order_cost(self):
       cost = 0
       for item in self.order:
          cost += item.calculate_cost()
       return round(cost, 2)
    
    def order_tax(self):
       tax = 0
       for item in self.order:
          tax += item.calculate_tax()
       return round(tax, 2)
    
    def get_pay_type(self):
        if isinstance(self.pay_type, PayType):
            return self.pay_type
        else:
            raise ValueError
    
    def set_pay_type(self, new_pay_type: PayType):
        if isinstance(new_pay_type, PayType):
            self.pay_type = new_pay_type
        else:
            raise ValueError
        
    def sort(self):
       sorted_order = sorted(self.order, key=lambda item: item.calculate_cost())
       self.order = sorted_order
    
    def __str__(self):
      receipt = "-------------------------------------Receipt-------------------------------------\n"
      for item in self.order:
          receipt += f"{item}\n"
      receipt += "---------------------------------------------------------------------------------\n"
      receipt += f"Total number of items in order: {len(self)}\n"
      receipt += f"{'Order Subtotals:':53s} ${str(self.order_cost()):14s} [Tax: {self.order_tax()}]\n"
      receipt += f"{'Order Total:':74s} ${round(self.order_cost() + self.order_tax(), 2)}\n"
      receipt += "---------------------------------------------------------------------------------\n"
      receipt += f"Paid with {self.pay_type.value}"

      return receipt