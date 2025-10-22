

def test_smartphone(smartphone_one, smartphone_two, smartphone_three, lawngrass_one, lawngrass_two):
    assert smartphone_one.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_one.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_one.price == 180000.0
    assert smartphone_one.quantity == 5
    assert smartphone_one.efficiency == 95.5
    assert smartphone_one.model == "S23 Ultra"
    assert smartphone_one.memory == 256
    assert smartphone_one.color == "Серый"

    assert smartphone_two.name == "Iphone 15"
    assert smartphone_two.description == "512GB, Gray space"
    assert smartphone_two.price == 210000.0
    assert smartphone_two.quantity == 8
    assert smartphone_two.efficiency == 98.2
    assert smartphone_two.model == "15"
    assert smartphone_two.memory == 512
    assert smartphone_two.color == "Gray space"

    assert smartphone_three.name == "Xiaomi Redmi Note 11"
    assert smartphone_three.description == "1024GB, Синий"
    assert smartphone_three.price == 31000.0
    assert smartphone_three.quantity == 14
    assert smartphone_three.efficiency == 90.3
    assert smartphone_three.model == "Note 11"
    assert smartphone_three.memory == 1024
    assert smartphone_three.color == "Синий"

    assert lawngrass_one.name == "Газонная трава"
    assert lawngrass_one.description == "Элитная трава для газона"
    assert lawngrass_one.price == 500.0
    assert lawngrass_one.quantity == 20
    assert lawngrass_one.country == "Россия"
    assert lawngrass_one.germination_period == "7 дней"
    assert lawngrass_one.color == "Зеленый"

    assert lawngrass_two.name == "Газонная трава 2"
    assert lawngrass_two.description == "Выносливая трава"
    assert lawngrass_two.price == 450.0
    assert lawngrass_two.quantity == 15
    assert lawngrass_two.country == "США"
    assert lawngrass_two.germination_period == "5 дней"
    assert lawngrass_two.color == "Темно-зеленый"

def test_smartphone_add(smartphone_one, smartphone_two):
    assert smartphone_one + smartphone_two == 2580000.0
    assert 16750.0



