from prac07.car import Car


class UnreliableCar(Car):
    """Class to practise inheritance, Unreliable Car will generate random value when asked to drive"""

    def __init__(self, name, fuel, reliability=50.0):
        """Initialise a unreliable car instance
        reliability = float between 0 and 100 representing a percentage chance of success when drive
        method called
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        from random import randint
        if randint(0,100) < self.reliability:
            super().drive(distance)
