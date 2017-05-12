from prac8.taxi import Taxi

def main():
    prius_1 = Taxi("Prius 1", 100)
    prius_1.drive(40)
    print(prius_1)
    print(prius_1.get_fare())
main()
