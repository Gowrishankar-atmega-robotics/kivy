from kivymd.app import MDApp 
from kivymd.uix.screen import Screen 
from kivymd.uix.button import MDRectangleFlatButton 
from kivy.lang import Builder 
import helpers
class demo(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        scr = Screen();
        self.ent = Builder.load_string(helpers.HelpX)
        but = MDRectangleFlatButton(text="click",pos_hint = {'center_x': 0.5 , 'center_y': 0.5}, on_press = self.fn , on_release= self.fn1);
        scr.add_widget(but);
        return scr 
    def fn(self, obj):
        print("1")
    def fn1(self , obj):
        print("2")
demo().run()