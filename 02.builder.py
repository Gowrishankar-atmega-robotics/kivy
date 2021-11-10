from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder 

kv = """ 
Screen:
    MDTextField:
        hint_text : "User Name"
        helper_text : "or click here"
        helper_text_mode: "on_focus"
        icon_right: "Android"
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x': 0.5 , 'center_y':0.5}
        size_hint_x : None
        width:300

"""
class demo(MDApp):
    def build(self):
        scr = Screen();
        ent = Builder.load_string(kv);
        scr.add_widget(ent)
        return scr
demo().run()