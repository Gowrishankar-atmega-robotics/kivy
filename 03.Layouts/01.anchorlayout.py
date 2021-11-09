from kivy.app import App 
from kivy.uix.anchorlayout import AnchorLayout 
#from kivymd.uix.button import MDRectangleFlatButton 
from kivy.uix.button import Button
class demo(App):
    def build(self):
        lay = AnchorLayout();
        bt1 = Button(text = " Atmega World", font_size="12",background_color = (.5, .6, .5, .6),halign ="center",size_hint=(.12 , .12));
        lay.add_widget(bt1);
        return lay
demo().run();