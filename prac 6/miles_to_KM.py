"""
1404 Prac 6
kivy program to convert miles to kilometers
Keegan Bentley
Started on 9/04/2017
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometers(App):
    def build(self):
        Window.size = (400, 150)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_KM.kv')
        return self.root


    def increment_value(self, value, increment):
        adjustedValue = value + increment
        self.root.ids.input_number.text = str(adjustedValue)

    def convert_miles_to_km(self, value):
        result = value * 1.609344
        self.root.ids.output_label.text = str(result)


MilesToKilometers().run()
