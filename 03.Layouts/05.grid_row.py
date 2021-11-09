from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 

class demo(App):
    def build(self):
        lay = GridLayout(rows=4,row_force_default=True, row_default_height = 40);
        lay.add_widget(Button(text="ATMEGA",size_hint_x = None ));
        lay.add_widget(Button(text="ROBOTICS",size_hint_x = None));
        lay.add_widget(Button(text="AR",size_hint_x = None));
        lay.add_widget(Button(text="AR_UAVS",size_hint_x = None));
        return lay 
demo().run();