from kivymd.app import MDApp
from kivymd.uix.label import MDIcon
from kivymd.font_definitions import theme_font_styles

class demo(MDApp):
    def build(self):
        return MDIcon(icon = " language-python", halign="center");
demo().run()