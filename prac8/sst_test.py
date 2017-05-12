from prac8.silver_service_taxi import SilverServiceTaxi


def main():
    t = SilverServiceTaxi("t", 40, 2)
    print(t.flagfall)
    t.drive(20)
    print(t)
    print("${:.2f}".format(t.get_fare()))
main()