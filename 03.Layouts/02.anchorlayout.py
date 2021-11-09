from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.anchorlayout import AnchorLayout 

class demo(App):
    def build(self):
        lay = AnchorLayout(anchor_x="left",anchor_y="top");
        but = Button(text="click here",font_size = "12", size_hint=(0.2 , 0.2),);
        lay.add_widget(but);
        return lay 
demo().run();