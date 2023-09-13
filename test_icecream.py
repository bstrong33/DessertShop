from dessert import DessertItem, IceCream

def test_icecream_init():
    i = IceCream()
    assert i.name == ""
    assert i.tax_percent == 7.25
    assert i.scoop_count == 0
    assert i.price_per_scoop == 0.0
    assert i.packaging == "Bowl"

    i = IceCream("vanilla", 8.25, 1, 2.5)
    assert i.name == "vanilla"
    assert i.tax_percent == 8.25
    assert i.scoop_count == 1
    assert i.price_per_scoop == 2.5
    assert i.packaging == "Bowl"

    assert issubclass(IceCream, DessertItem)
    assert isinstance(i, DessertItem)

def test_icecream_calculate_cost():
    i = IceCream("Pistachio", 7.25, 2, .79)
    assert i.calculate_cost() == 1.58

def test_icecream_calculate_tax():
    i = IceCream("Pistachio", 7.25, 2, .79)
    assert i.calculate_tax() == .11
