from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton 

class demo(MDApp):
    def build(self):
        scr = Screen();
        but = MDRectangleFlatButton(text="Click here",font_size="30sp",theme_text_color="Custom", text_color = (.4, .5, .6 , .7) , pos = (0, 0));
        
        scr.add_widget(but);
        return scr
demo().run();
        