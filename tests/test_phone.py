# tests/test_phone.py
from src.phone import Phone
import pytest

def test_phone_creation():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone) == "iPhone 14"
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone.number_of_sim == 2

def test_phone_invalid_number_of_sim():
    with pytest.raises(ValueError):
        Phone("iPhone 14", 120000, 5, 0)

    with pytest.raises(ValueError):
        Phone("iPhone 14", 120000, 5, -1)

    with pytest.raises(ValueError):
        Phone("iPhone 14", 120000, 5, "two")

def test_phone_addition():
    from src.item import Item

    phone1 = Phone("iPhone 14", 120000, 5, 2)
    phone2 = Phone("iPhone 13", 100000, 3, 1)
    item = Item("Смартфон", 10000, 20)

    assert phone1 + phone2 == 8
    assert phone1 + item == 25
    assert item + phone2 == 23

    with pytest.raises(TypeError):
        phone1 + "invalid"