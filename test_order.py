import pytest
from collections.abc import Iterator
from dessert import Order, Cookie, IceCream, Candy
from payable import PayType

def test_order_init():
    o = Order()
    assert o.order == []
    assert o.pay_type == PayType.CASH

def test_order_add():
    o = Order()
    o.add(Cookie("snickerdoodle", 7.25, 12, 5.5))
    assert o.order[0].name == "snickerdoodle"
    assert o.order[0].cookie_quantity == 12
    assert o.order[0].price_per_dozen == 5.5

def test_order_len():
    o = Order()
    assert len(o) == 0

    o.add(IceCream("vanilla", 7.25, 1, 2.5))
    assert len(o) == 1

    o.add(Cookie("snickerdoodle", 7.25, 12, 5.5))
    assert len(o) == 2
    assert len(o) != 3

def test_order_iter():
    o = Order()
    assert isinstance (o, Iterator)

def test_order_next():
    o = Order()
    obj = iter(o)
    o.add(IceCream("vanilla", 7.25, 1, 2.5))
    o.add(Cookie("snickerdoodle", 7.25, 12, 5.5))
    assert next(obj) == o.order[0]
    assert next(obj) == o.order[1]
    assert next(obj) == None

def test_order_get_pay_type():
    o = Order()
    assert o.get_pay_type() == PayType.CASH

    with pytest.raises(ValueError):
        o.pay_type = "CHECK"
        o.get_pay_type()    

def test_order_set_pay_type():
    o = Order()

    o.set_pay_type(PayType.CARD)
    assert o.pay_type.value == "CARD"

    o.set_pay_type(PayType.PHONE)
    assert o.pay_type == PayType.PHONE

    with pytest.raises(ValueError):
        o.set_pay_type("CHECK")

def test_order_sort():
    o = Order()
    o.add(Candy("Candy Corn", 7.25, 1.5, .25))  # $0.38
    o.add(Candy("Gummy Bears", 7.25, .25, .35)) # $0.09
    o.add(IceCream("Pistachio", 7.25, 2, .79))  # $1.58
    o.add(Cookie("Oatmeal Raisin", 7.25, 2, 3.45))  # $0.58

    assert o.order[0] == Candy("Candy Corn", 7.25, 1.5, .25)
    assert o.order[3] == Cookie("Oatmeal Raisin", 7.25, 2, 3.45)

    o.sort()

    assert o.order[0] == Candy("Gummy Bears", 7.25, .25, .35)   # $0.09
    assert o.order[1] == Candy("Candy Corn", 7.25, 1.5, .25)    # $0.38
    assert o.order[2] == Cookie("Oatmeal Raisin", 7.25, 2, 3.45)    # $0.58
    assert o.order[3] == IceCream("Pistachio", 7.25, 2, .79)    # $1.58

