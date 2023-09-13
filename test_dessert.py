from dessert import DessertItem, Candy, Cookie

def test_dessertitem_init():
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

def test_dessertitem_relational_operators():
    c1 = Candy("Candy Corn", 7.25, 1.5, .25)
    c2 = Candy("Candy Corn", 7.25, 1.5, .25)
    co = Cookie("Oatmeal Raisin", 7.25, 2, 3.45)

    assert (c1 == c2) == True
    assert (c1 != c2) == False
    assert (c1 < c2) == False
    assert (c1 > c2) == False
    assert (c1 >= c2) == True
    assert (c1 <= c2) == True

    assert (c1 == co) == False
    assert (c1 != co) == True
    assert (c1 < co) == True
    assert (c1 > co) == False
    assert (c1 >= co) == False
    assert (c1 <= co) == True

    