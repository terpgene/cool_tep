# Public => memberName
# Protected => _memberName
# Private => __memberName

class Car:
    numberOfWheels = 4
    _color = "Black"


class BMW(Car):
    def __init__(self):
        print("Protected attribute color: ", self._color)

car = Car()
print("Publice attribute numberOfWheels: ", car.numberOfWheels)
bmw = BMW()