"""
1404 Prac 6
Kivy program to practice dynamically creating widgets
started 10/4/17
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list = ['label 1', 'label 2', 'label 3', 'label 4']

    def build(self):
        self.title = 'List of Labels'
        self.root = Builder.load_file('dynamic_widget.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for value in self.list:
            temp_label = Label(text=value)
            self.root.ids.dynamicBox.add_widget(temp_label)

DynamicWidgetsApp().run()