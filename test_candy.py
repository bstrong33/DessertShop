from dessert import DessertItem, Candy, Cookie

def test_candy_init():
    c = Candy()
    assert c.name == ""
    assert c.tax_percent == 7.25
    assert c.weight == 0.0
    assert c.price_per_pound == 0.0
    assert c.packaging == "Bag"

    c = Candy("jelly bean", 8.25, 1.5, 3.5)
    assert c.name == "jelly bean"
    assert c.tax_percent == 8.25
    assert c.weight == 1.5
    assert c.price_per_pound == 3.5
    assert c.packaging == "Bag"

    assert issubclass(Candy, DessertItem)
    assert isinstance(c, DessertItem)

def test_candy_calculate_cost():
    c = Candy("Candy Corn", 7.25, 1.5, .25)
    assert c.calculate_cost() == .38

def test_candy_calculate_tax():
    c = Candy("Candy Corn", 7.25, 1.5, .25)
    assert c.calculate_tax() == .03

def test_candy_can_combine():
    c1 = Candy("Candy Corn", 7.25, 1.5, .25)
    c2 = Candy("Candy Corn", 7.25, 2, .25)
    co = Cookie("Chocolate Chip", 7.25, 6, 3.99)

    assert c1.can_combine(c2) == True
    assert c1.can_combine(co) == False

def test_candy_combine():
    c1 = Candy("Candy Corn", 7.25, 1.5, .25)
    c2 = Candy("Candy Corn", 7.25, 2, .25)
    co = Cookie("Chocolate Chip", 7.25, 6, 3.99)

    c1.combine(c2)
    assert c1.weight == 3.5

    c1.combine(co)
    assert c1.weight == 3.5