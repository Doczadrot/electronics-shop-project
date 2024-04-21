# src/phone.py
from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.validate_number_of_sim(number_of_sim)
        self.number_of_sim = number_of_sim

    def validate_number_of_sim(self, number_of_sim):
        if not isinstance(number_of_sim, int) or number_of_sim <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other):
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity
        else:
            raise TypeError("Можно складывать только экземпляры классов Item и Phone.")

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"