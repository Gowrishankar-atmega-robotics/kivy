from kivy.app import App 
from kivy.uix.switch import Switch 
class demo(App):
    def build(self):
        click = Switch(active = True)
        return click

demo().run()