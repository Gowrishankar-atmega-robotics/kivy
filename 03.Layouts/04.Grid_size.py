from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 

class demo(App):
    def build(self):
        lay = GridLayout(cols=4,row_force_default = True ,row_default_height=60);
        lay.add_widget(Button(text="hello"));
        lay.add_widget(Button(text="atmega"));
        lay.add_widget(Button(text="world"));
        lay.add_widget(Button(text="robotics"));
        return lay
demo().run();