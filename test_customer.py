from dessertshop import Customer
from dessert import Order, Candy, Cookie

def test_customer_init():
    cus1 = Customer("Matt")
    cus2 = Customer("John")
    assert cus1.customer_name == "Matt"
    assert cus1.order_history == []
    assert cus1.customer_id == 0
    assert cus1.customer_id != cus2.customer_id
    assert cus2.customer_id == 1

def test_customer_add2history():
    o = Order()
    o.add(Candy("Candy Corn", 7.25, 1.5, .25))
    o.add(Cookie("Chocolate Chip", 7.25, 6, 3.99))
    cus = Customer("Emma")
    cus.add2history(o)

    assert cus.order_history[0].order[0] == Candy("Candy Corn", 7.25, 1.5, .25)
    assert cus.order_history[0].order[1] == Cookie("Chocolate Chip", 7.25, 6, 3.99)

