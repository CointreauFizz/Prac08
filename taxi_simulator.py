from SilverService_Taxi import SilverServiceTaxi
from taxi2 import Taxi2


def main():
    print("Let's Drive")
    taxi_list = [Taxi2("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    current_taxi = None
    main_menu(taxi_list, total_bill, current_taxi)


def main_menu(taxi_list, total_bill, current_taxi):
    while True:
        menu = "q)uit, c)hoose taxi, d)rive"
        print(menu)
        choice = input(">>> ").lower()
        choice = validate_input(choice)

        if choice == "c":
            choice = ""
            current_taxi = display_taxis(taxi_list)
            print("Bill to date ${:.2f}".format(total_bill))

        if choice == "d":
            choice = ""
            if current_taxi is None:
                print("choose a taxi")
                main_menu(taxi_list, total_bill, current_taxi)
            else:
                drive_a_taxi(current_taxi)
                total_bill = total_bill + current_taxi.get_fare()
                print("Bill to date ${:.2f}".format(total_bill))

        if choice == "q":
            print("Total Cost is: ${:.2f}".format(total_bill))
            print("Taxis are now:")
            for i in range(len(taxi_list)):
                print("{}".format(i), taxi_list[i])
            raise SystemExit(0)


def validate_input(choice):
    while choice != "c" and choice != "q" and choice != "d":
        print("wrong input. please try again")
        choice = input(">>> ").lower()
    return choice


def display_taxis(taxi_list):
    print("taxis available:")
    for i in range(len(taxi_list)):
            print("{}".format(i), taxi_list[i])
    preferred = int(input("Choose your taxi: "))
    while preferred > len(taxi_list) or preferred < 0:
        preferred = int(input("Wrong input....Please select a taxi: "))
    return taxi_list[preferred]


def drive_a_taxi(current_taxi):
    distance = int(input("Drive how far? "))
    while distance <= 0:
        distance = input("ERROR!...try again: ")
    fare_price = distance * current_taxi.price_per_km
    print("Your {} trip cost you ${:.2f}".format(current_taxi.name, fare_price))
    current_taxi.drive(distance)
    return current_taxi


if __name__ == '__main__':
    main()
