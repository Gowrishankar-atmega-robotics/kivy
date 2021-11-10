from kivy.app import App 
from kivy.uix.textinput import TextInput 

class demo(App):
    def build(self):
        return TextInput(text = "text here")
demo().run()