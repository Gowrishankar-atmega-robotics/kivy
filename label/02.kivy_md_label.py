from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.label import MDLabel

class demo(MDApp):
    def build(self):
        return MDLabel(text="Hello world", halign ="center", font_style = "Caption",pos=(0,100));
Demo = demo();
Demo.run();