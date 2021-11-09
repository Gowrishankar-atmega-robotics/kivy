from kivymd.app import MDApp
from kivymd.uix.label import MDIcon, MDLabel
from kivymd.font_definitions import theme_font_styles

class demo(MDApp):
    def build(self):
        lb = MDLabel(text="themes", halign = "center", font_style ="H2", theme_text_color = "Primary")
        return lb
#d = demo();
#d.run();
demo().run();