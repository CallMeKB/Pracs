from prac07.car import Car


def main():
    bus = Car("Bus", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print("limo fuel = ", limo.fuel)
    limo.drive(115)
    print("limo odo =", limo.odometer)
    print(bus)
    print(limo)
main()
