"""CP1404 Prac 8 - Inheritance  
Program which lets user choose a taxi from a list and drive it a certain distance, 
the program will keep track of the users total bill as they move between cars
"""
from prac8.taxi import Taxi
from prac8.silver_service_taxi import SilverServiceTaxi

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


main()