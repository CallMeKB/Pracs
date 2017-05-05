from prac8.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Class for 'fancier' taxis"""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise an instance of SilverServiceTaxi
        flagfall = extra charge for new fare
        fanciness = multiplier for price per km
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        """return a string like Taxi but with flagfall included"""
        return "{} plus flagfall of {}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """return a float like Taxi but with flagfall included"""
        return super().get_fare() + self.flagfall
