from kivy.app import App 
from kivy.uix.relativelayout import RelativeLayout 
from kivy.uix.button import Button 

class demo(App):
    def build(self):
        lay = RelativeLayout();
        bt = Button(text="click here",size_hint=(.1 , .1),pos=(300, 300));
        return bt

demo().run();