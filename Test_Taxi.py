
from taxi import Taxi
from taxi2 import Taxi2

taxi1 = Taxi("prius 1", 100, 1.23)
taxi1.drive(40)
print(taxi1)
taxi1.start_fare()
taxi1.drive(100)
print(taxi1)

taxi1 = Taxi2("prius 1", 100)
taxi1.drive(40)
print(taxi1)
taxi1.start_fare()
taxi1.drive(100)
print(taxi1)

