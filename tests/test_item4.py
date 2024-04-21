# tests/test_item.py
from src.item import Item
from src.phone import Phone

def test_item_addition():
    item1 = Item("Товар 1", 100, 5)
    item2 = Item("Товар 2", 200, 10)
    phone = Phone("iPhone 14", 120000, 3, 2)

    assert item1 + item2 == 15
    assert item1 + phone == 8
    assert phone + item2 == 13