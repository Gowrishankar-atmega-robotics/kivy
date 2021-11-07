from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

from kivymd.font_definitions import theme_font_styles

class demo(MDApp):
    def build(self):
        return MDLabel(text="Custom", halign = "right",font_style="H2",  theme_text_color = "Custom", text_color=(0 , 0 , 0 , 1));

demo().run()