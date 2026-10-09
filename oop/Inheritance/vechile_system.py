class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Year  : {self.year}")

    def start(self):
        print(f"{self.brand} {self.model}: Vehicle start ho rahi hai")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Doors : {self.num_doors}")

    def start(self):
        print(f"{self.brand} {self.model}: Car engine start ho rahi hai 🔑")

    def honk(self):
        print("Beep Beep! 📢")


class Bike(Vehicle):
    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc

    def display_info(self):
        super().display_info()
        print(f"Engine : {self.engine_cc} CC")

    def start(self):
        print(f"{self.brand} {self.model}: Bike kick se start ho rahi hai 🦵")

class Truck(Vehicle):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def display_info(self):
        super().display_info()
        print(f"Load Capacity : {self.load_capacity}")

    def start(self):
        print(f"{self.brand} {self.model}: Truck diesel se start ho raha hai")

    def load_cargo(self, weight):
        if weight <= self.load_capacity:
            print(f"✅ {weight}kg cargo loaded in {self.brand} {self.model}")
        else:
            print(f"❌ Overload! {weight}kg > {self.load_capacity}kg capacity")



# ===== Test =====
print("=" * 40)
print("🚗 CAR DETAILS")
print("=" * 40)
c = Car("Toyota", "Camry", 2023, 4)
c.display_info()
c.start()
c.honk()

print("\n" + "=" * 40)
print("🏍️  BIKE DETAILS")
print("=" * 40)
b = Bike("Honda", "CBR", 2022, 150)
b.display_info()
b.start()

print("\n" + "=" * 40)
print("🏍️  Truck DETAILS")
print("=" * 40)
t= Truck("Tata", "A890", 2019, 500)
t.display_info()
t.start()
t.load_cargo(1000)

# __str__ test
print(f"\nVehicle: {c}")
print(f"Vehicle: {b}")
print(f"Vehicle: {t}")
