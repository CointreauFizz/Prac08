
from Unreliable_Car import UnreliableCar

car1 = UnreliableCar("Good", 100, 80)
car2 = UnreliableCar("Bad", 100, 9)

for i in range(1, 12):
    print("Drives {}km:".format(i))
    print()
    print("{:12} drove {:2}km".format(car1.name, car1.drive(i)))
    print("{:12} drove {:2}km".format(car2.name, car2.drive(i)))

print(car1)
print(car2)
