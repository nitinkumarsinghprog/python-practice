# Parent 1: Car
#   - method: drive() -> "Car chal rahi hai"
#   - method: honk() -> "Beep Beep!"
#
# Parent 2: Airplane
#   - method: fly() -> "Plane udd raha hai"
#   - method: land() -> "Plane land kar raha hai"
#
# Child: FlyingCar(Car, Airplane)
#   - dono ke methods access kar sake
#   - extra: method: transform() -> "Car se Plane ban gaya!"
#
# Test karo: FlyingCar object banao, sab methods call karo

class Car:
    def drive(self):
        return "🚗 Car chal rahi hai"

    def honk(self):
        return "📢 Beep Beep!"    

class Airplane:
    def fly(self):
        return "✈️ Plane udd raha hai"

    def land(self):
        return "🛬 Plane land kar raha hai"

class FlyingCar(Car, Airplane):
    def transform(self):
        return "🔄 Car se Plane ban gaya!"


# FlyingCar object banao
fc = FlyingCar()

# Sab methods call karo
print(fc.drive())       # Car se
print(fc.honk())        # Car se
print(fc.fly())         # Airplane se
print(fc.land())        # Airplane se
print(fc.transform())   # FlyingCar ka apna