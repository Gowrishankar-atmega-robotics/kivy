import kivy
from kivy.app import App 
from kivy.uix.label import Label

class Demo(App):
    def build(self):
        lb = Label(text="hello world")
        return lb
demo= Demo()
demo.run();