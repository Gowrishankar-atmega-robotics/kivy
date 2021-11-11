from kivymd.app import MDApp 
from kivymd.uix.screen import Screen
from kivy.lang import Builder 
from helpers import HelpX

class demo(MDApp):
    def build(self):
        scr = Screen();
        ef = Builder.load_string(helpers.HelpX)
        scr.add_widget(ef);
        return scr 
demo().run()