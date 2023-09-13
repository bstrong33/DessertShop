from dessert import DessertItem, Candy, Cookie, IceCream, Sundae, Order
from payable import PayType
#from receipt import make_receipt

class DessertShop:
    customer_db: dict = {}

    def user_prompt_candy(self):
        while True:
            try:
                name = input("Enter the type of candy: ")
                weight = int(input("Enter the weight in pounds: "))
                price = float(input("Enter the price per pound: "))
            except:
                print("It looks like you typed an invalid value, please try again")
            else:
                return Candy(name, 7.25, weight, price)
    
    def user_prompt_cookie(self):
        while True:
            try:
                name = input("Enter the type of cookie: ")
                quantity = int(input("Enter the quantity purchased: "))
                price = float(input("Enter the price per dozen: "))
            except:
                print("It looks like you typed an invalid value, please try again")
            else:
                return Cookie(name, 7.25, quantity, price)

    def user_prompt_icecream(self):
        while True:
            try:
                name = input("Enter the type of ice cream: ")
                scoops = int(input("Enter the number of scoops: "))
                price = float(input("Enter the price per scoop: "))
            except:
                print("It looks like you typed an invalid value, please try again")
            else:
                return IceCream(name, 7.25, scoops, price)

    def user_prompt_sundae(self):
        while True:
            try:
                name = input("Enter the type of ice cream: ")
                scoops = int(input("Enter the number of scoops: "))
                price = float(input("Enter the price per scoop: "))
                topping = input("Enter the topping: ")
                topping_price = float(input("Enter the price for the topping: "))
            except:
                print("It looks like you typed an invalid value, please try again")
            else:
                return Sundae(name, 7.25, scoops, price, topping, topping_price)
    
    def user_prompt_payment(self):
       while True:
          try:
            payment = int(input("1: Cash\n2: Card\n3: Phone\nEnter payment method: "))
            if payment not in [1, 2, 3]:
               raise ValueError
          except:
             print("\nPlease submit a payment type by typing 1, 2, or 3\n")
          else:
             pay_type = PayType.CASH
             if payment == 2:
                pay_type = PayType.CARD
             elif payment == 3:
                pay_type = PayType.PHONE
             return pay_type

class Customer:
   id: int = 0

   def __init__(self, customer_name):
      self.customer_name = customer_name
      self.order_history = []
      self.customer_id = Customer.id
      Customer.id += 1
    
   def add2history(self, order: Order):
      self.order_history.append(order)
      return self


def main():
    make_new_order: bool = True
    while make_new_order:
      shop = DessertShop()
      order = Order()

      # print(PayType.get_pay_type(PayType))
      # PayType.set_pay_type(PayType, "CARd")
      # print(PayType.get_pay_type(PayType))

      '''
      order.add(Candy("Candy Corn", 7.25, 1.5, .25))
      order.add(Candy("Gummy Bears", 7.25, .25, .35))
      order.add(Cookie("Chocolate Chip", 7.25, 6, 3.99))
      order.add(IceCream("Pistachio", 7.25, 2, .79))
      order.add(Sundae("Vanilla", 7.25, 3, .69, "Hot Fudge", 1.29))
      order.add(Cookie("Oatmeal Raisin", 7.25, 2, 3.45))
      '''

      # boolean done = false
      done: bool = False
      
      # build the prompt string once
      prompt = '\n'.join([ '\n',
              '1: Candy',
              '2: Cookie',            
              '3: Ice Cream',
              '4: Sunday',
              '5: Admin Module'
              '\nWhat would you like to add to the order? (1-5, Enter for done): '
        ])
      
      admin_prompt = '\n'.join(['\n',
                      '1: Shop Customer List',
                      '2: Customer Order History',
                      '3: Best Customer',
                      '4: Exit Admin Module',
                      '\nWhich option would you like?: '])

      while not done:
        choice = input(prompt)
        match choice:
          case '':
            done = True
          case '1':            
            item = shop.user_prompt_candy()
            order.add(item)
            print(f'{item.name} has been added to your order.')
          case '2':            
            item = shop.user_prompt_cookie()
            order.add(item)
            print(f'{item.name} has been added to your order.')
          case '3':            
            item = shop.user_prompt_icecream()
            order.add(item)
            print(f'{item.name} has been added to your order.')
          case '4':            
            item = shop.user_prompt_sundae()
            order.add(item)
            print(f'{item.name} has been added to your order.')
          case '5':
              admin_done: bool = False
              while not admin_done:
                admin_choice = input(admin_prompt)
                match admin_choice:
                  case '1':
                      for customer in shop.customer_db.values():
                        print(f"Customer Name: {customer.customer_name:15s} Customer ID: {customer.customer_id}")
                  case '2':
                      name = input("Enter the name of the customer: ")
                      if name not in shop.customer_db:
                         print("\nIt looks like that person isn't in the database")
                      else:
                         order_num = 1
                         print(f"\nCustomer Name: {name:15s} Customer ID: {shop.customer_db[name].customer_id}")
                         print("---------------------------------------------------------------------------------")
                         for ind_order in shop.customer_db[name].order_history:
                            print(f"Order #: {order_num}")
                            print(ind_order)
                            order_num += 1
                  case '3':
                      if shop.customer_db == {}:
                         print("It looks like there aren't any customers yet")
                      else:
                        def customer_total(customer):
                          total = 0
                          for i_order in customer.order_history:
                              total += i_order.order_cost()
                          return total
                        sorted_customers = sorted(shop.customer_db.values(), key = customer_total)
                        print("---------------------------------------------------------------------------------")
                        print(f"The Dessert Shop's most valued customer is: {sorted_customers[-1].customer_name}!")
                        print("---------------------------------------------------------------------------------")
                  case '4':
                      admin_done = True
                  case _:
                      print('Invalid response:  Please enter a choice from the menu (1-4)')
          case _:            
            print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')
      print()

    #
    #add your code below here to print the PDF receipt as the last thing in main()
    #

      
      order.add(Candy("Candy Corn", 7.25, 1.5, .25))
      order.add(Candy("Gummy Bears", 7.25, .25, .35))
      order.add(Cookie("Chocolate Chip", 7.25, 6, 3.99))
      order.add(IceCream("Pistachio", 7.25, 2, .79))
      order.add(Sundae("Vanilla", 7.25, 3, .69, "Hot Fudge", 1.29))
      order.add(Cookie("Oatmeal Raisin", 7.25, 2, 3.45))
      
      

      '''
      data = [["Name", "Item Cost", "Tax"]]
      for item in order.order:
        lst = [item.name, item.calculate_cost(), item.calculate_tax()]
        data.append(lst)
      data.append(["---------------------------------------", "", ""])
      data.append(["Order Subtotals", order.order_cost(), order.order_tax()])
      data.append(["Order Total", "", order.order_cost() + order.order_tax()])
      data.append(["Total items in the order", "", len(order)])
      
      make_receipt(data, "receipt.pdf")
      '''

      # Get customer name and verify if in customer_db, add order to given customer
      cust_name = input("Enter the customer name: ")
      if cust_name not in shop.customer_db:
         shop.customer_db[cust_name] = Customer(cust_name)
      
      shop.customer_db[cust_name].add2history(order)

      
      # Getting payment type from user and setting this value in the order
      pay_type = shop.user_prompt_payment()
      order.set_pay_type(pay_type)

      customer = shop.customer_db[cust_name]

      print(f"\nCustomer Name: {customer.customer_name:17s} Customer ID: {str(customer.customer_id):18s} Total Orders: {len(customer.order_history)}")

      order.sort()
      print(order)

      new_order = input("Would you like to start a new order? Type 'y' for yes and 'n' for no: " )
      if new_order != "y":
         make_new_order = False


if __name__ == "__main__":
   main()
