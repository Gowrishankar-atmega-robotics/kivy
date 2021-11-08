import os
os.environ["KIVY_TEXT"]="pil"
from kivymd.app import MDApp 
from kivymd.uix.button import MDRoundFlatIconButton 

class demo(MDApp):
    def build(self):
        but = MDRoundFlatIconButton(text="Atmega",pos=(350,500));
        return but ;
demo().run();