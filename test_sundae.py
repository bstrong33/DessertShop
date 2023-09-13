from dessert import DessertItem, Sundae

def test_sundae_init():
    s = Sundae()
    assert s.name == ""
    assert s.tax_percent == 7.25
    assert s.scoop_count == 0
    assert s.price_per_scoop == 0.0
    assert s.topping_name == ""
    assert s.topping_price == 0.0
    assert s.packaging == "Boat"

    s = Sundae("caramel vanilla", 8.25, 1, 2.5, "caramel", 1.5)
    assert s.name == "caramel vanilla"
    assert s.tax_percent == 8.25
    assert s.scoop_count == 1
    assert s.price_per_scoop == 2.5
    assert s.topping_name == "caramel"
    assert s.topping_price == 1.5
    assert s.packaging == "Boat"

    assert issubclass(Sundae, DessertItem)
    assert isinstance(s, DessertItem)

def test_sundae_calculate_cost():
    s = Sundae("Vanilla", 7.25, 3, .69, "Hot Fudge", 1.29)
    assert s.calculate_cost() == 3.36

def test_sundae_calculate_tax():
    s = Sundae("Vanilla", 7.25, 3, .69, "Hot Fudge", 1.29)
    assert s.calculate_tax() == .24
