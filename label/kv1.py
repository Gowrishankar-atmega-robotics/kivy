import os 
os.environ["KIVY_TEXT"] = "pil"
from kivymd.app import MDApp
from kivy.lang import Builder

k = '''
Screen:
    BoxLayout:
        orientation : "vertical"
        MDToolbar:
            title: "Atmega"
            icon : "Git"
            type : "top"
            left_action_items:[["menu",lambda x : x]]
            md_bg_color: (0, 0 , 0, 0.55)
        MDLabel:
            text:"hello atmega"
            halign: "center"

'''

class test(MDApp):
    def build(self):
        return Builder.load_string(k)
test().run()