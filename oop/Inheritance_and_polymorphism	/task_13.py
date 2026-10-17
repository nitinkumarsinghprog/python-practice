# Product
#   - __init__(name, price, product_id)
#   - method: display() -> "Product: {name}, Price: ₹{price}, ID: {product_id}"
#
# Electronics(Product)
#   - __init__(name, price, product_id, brand, warranty)
#   - override display() -> parent + brand + warranty
#
# Mobile(Electronics)
#   - __init__(name, price, product_id, brand, warranty, ram, storage)
#   - override display() -> parent + ram + storage
#
# Smartphone(Mobile)
#   - __init__(name, price, product_id, brand, warranty, ram, storage, has_5g, os)
#   - override display() -> parent + has_5g + os
#
# Test karo: Smartphone object banao, display() call karo

class Product:
    def __init__(self, name, price, product_id ):
        self.name = name
        self.price = price
        self.product_id = product_id

    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: ₹{self.price}")
        print(f"ID: {self.product_id}")

class Electronics(Product):
    def __init__(self, name, price, product_id, brand, warranty):
        super().__init__(name, price, product_id)
        self.brand = brand
        self.warranty = warranty

    def display(self):
        super().display()
        print(f"Brand: {self.brand}")
        print(f"Warranty: {self.warranty}")

class Mobile(Electronics):
    def __init__(self, name, price, product_id, brand, warranty, ram, storage):
        super().__init__(name, price, product_id, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display(self):
        super().display()
        print(f"Ram: {self.ram}")
        print(f"Storage: {self.storage}")

class Smartphone(Mobile):
    def __init__(self, name, price, product_id, brand, warranty, ram, storage, has_5g, os):
        super().__init__(name, price, product_id, brand, warranty, ram, storage)
        self.has_5g = has_5g
        self.os = os

    def display(self):
        super().display()
        print(f"5G: {self.has_5g}")
        print(f"OS: {self.os}")


sm = Smartphone("Iphone 15", "79999", "P001", "Apple", "1 Year", "8 GB", "256 GB", "Yes","iOS 17")

sm.display()