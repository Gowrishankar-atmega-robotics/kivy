from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.font_definitions import theme_font_styles
class demo(MDApp):
    def build(self):
        return Button(text="click here", halign = "left", pos=(0 , 0))
demo().run();