from kivy.app import App 
from kivy.uix.switch import Switch 

class demo(App):
    def build(self):
        sw = Switch();
        sw.bind(active = self.state);
        return sw 
    def state(self ,i , value ):
        print(value);
demo().run();