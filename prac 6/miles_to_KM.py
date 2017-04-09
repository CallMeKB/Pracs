"""
1404 Prac 6
kivy program to convert miles to kilometers
Keegan Bentley
Started on 9/04/2017
"""

from kivy.app import App
from kivy.lang import Builder


class MilesToKilometers(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_KM.kv')
        return self.root


MilesToKilometers().run()
