from dessert import DessertItem, Cookie, Candy

def test_cookie_init():
    co = Cookie()
    assert co.name == ""
    assert co.tax_percent == 7.25
    assert co.cookie_quantity == 0
    assert co.price_per_dozen == 0.0
    assert co.packaging == "Box"

    co = Cookie("snickerdoodle", 8.25, 12, 5.5)
    assert co.name == "snickerdoodle"
    assert co.tax_percent == 8.25
    assert co.cookie_quantity == 12
    assert co.price_per_dozen == 5.5
    assert co.packaging == "Box"

    assert issubclass(Cookie, DessertItem)
    assert isinstance(co, DessertItem)

def test_cookie_calculate_cost():
    c = Cookie("Chocolate Chip", 7.25, 6, 3.99)
    assert c.calculate_cost() == 2.00

def test_cookie_calculate_tax():
    c = Cookie("Chocolate Chip", 7.25, 6, 3.99)
    assert c.calculate_tax() == .14

def test_cookie_can_combine():
    co1 = Cookie("Chocolate Chip", 7.25, 6, 3.99)
    co2 = Cookie("Chocolate Chip", 7.25, 4, 3.99)
    c = Candy("Candy Corn", 7.25, 1.5, .25)

    assert co1.can_combine(co2) == True
    assert co1.can_combine(c) == False

def test_cookie_combine():
    co1 = Cookie("Chocolate Chip", 7.25, 6, 3.99)
    co2 = Cookie("Chocolate Chip", 7.25, 4, 3.99)
    c = Candy("Candy Corn", 7.25, 1.5, .25)

    co1.combine(co2)
    assert co1.cookie_quantity == 10

    co1.combine(c)
    assert co1.cookie_quantity == 10
