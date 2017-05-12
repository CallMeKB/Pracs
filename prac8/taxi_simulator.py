"""CP1404 Prac 8 - Inheritance  
Program which lets user choose a taxi from a list and drive it a certain distance, 
the program will keep track of the users total bill as they move between cars
"""
from prac8.taxi import Taxi
from prac8.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def get_current_price(taxi_list):
    """return a total fare cost"""
    total = 0
    for taxi in taxi_list:
        if taxi.current_fare_distance > 0:
            total += taxi.get_fare()
    return total


def get_menu_choice():
    """get and validate users menu input, then return"""
    choice = input(">>>").lower()
    while choice != 'q' and choice != 'c' and choice != 'd':
        print("Invalid menu option.")
        choice = input(">>>").lower()
    return choice


def get_taxi_choice():
    """get and validate the users choice of taxi"""
    valid = False
    while not valid:
        try:
            choice = int(input("Choose taxi: "))
            valid = True
        except ValueError:
            print("Please enter a valid number.")
    return choice


def display_taxis(taxi_list):
    """format and print the taxis in their current state"""
    count = 0
    for taxi in taxi_list:
        print("{} - {}".format(count, taxi))
        count += 1


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(MENU)
    menu_choice = get_menu_choice()
    while menu_choice != 'q':
        if menu_choice == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = taxis[get_taxi_choice()]
        elif menu_choice == 'd':
            trip_distance = int(input("Drive how far? "))
            pre_fare_total = get_current_price([current_taxi])
            drove = current_taxi.drive(trip_distance)

            trip_fare = current_taxi.get_fare() - pre_fare_total
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_fare))
        print("Bill to date: ${:.2f}".format(get_current_price(taxis)))
        print(MENU)
        menu_choice = get_menu_choice()
    print("Total trip cost: ${:.2f}".format(get_current_price(taxis)))
    print("Taxis are now:")
    display_taxis(taxis)


main()