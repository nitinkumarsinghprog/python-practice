class Product:
    def __init__(self, name, price, quantity):
        self.name = name

        if price > 0:
            self.price = price
        else:
            raise ValueError("Invalid price of the item")

        if quantity >= 0:
            self.quantity = quantity
        else:
            raise ValueError("Invalid quantity of the item")

    def display_product(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")

    def update_price(self, new_price):
        if new_price > 0:
            self.price = new_price
        else:
            raise ValueError("Invalid price of the item")

    def calculate_total(self):
        return self.price * self.quantity


product = Product("Laptop", 60000, 2)

product.display_product()

print("Total:", product.calculate_total())

product.update_price(55000)

print("After price update:")
print("Total:", product.calculate_total())