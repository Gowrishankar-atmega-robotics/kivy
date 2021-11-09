from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout 

class demo(App):
    def build(self):
        lay = GridLayout(cols=2);
        bt = Button(text="click here", size_hint=(.1 , .1));
        bt1 = Button(text="atmega",size_hint=(.1 , .1 ))
        lay.add_widget(bt);
        lay.add_widget(bt1)
        return lay 
demo().run()