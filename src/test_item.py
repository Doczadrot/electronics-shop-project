import pytest
from src.item import Item

@pytest.fixture(autouse=True)
def clear_item_all():
    # Очищаем список all перед каждым тестом
    Item.all.clear()
    yield  # Выполняем тест
    # Очищаем список all после каждого теста
    Item.all.clear()

def test_calculate_total_price():
    item = Item("Phone", 100, 5)
    assert item.calculate_total_price() == 500

def test_apply_discount():
    item = Item("Laptop", 1000, 3)
    item.pay_rate = 0.7  # Apply a 30% discount
    item.apply_discount()
    assert item.price == 700

def test_item_all():
    item1 = Item("Phone", 100, 1)
    item2 = Item("Laptop", 1000, 3)
    item3 = Item("Cable", 10, 5)
    assert len(Item.all) == 3
    assert item1 in Item.all
    assert item2 in Item.all
    assert item3 in Item.all

def test_repr():
    item = Item("Phone", 100, 5)
    assert repr(item) == "Item('Phone', 100, 5)"