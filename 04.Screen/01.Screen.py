from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton 

class demo(MDApp):
    def build(self):
        scr = Screen();
        fb = MDFlatButton(text="AR World",size_hint=(.1 , .1 ),pos=(300,300));
        scr.add_widget(fb);
        return scr 
demo().run(); 