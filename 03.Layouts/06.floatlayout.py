from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.button import Button 

class demo(App):
    def build(self):
        lay = FloatLayout();
        but = Button(text="click here", size_hint=(.1 , .1),pos=(300,300))
        lay.add_widget(but)
        return lay
demo().run();