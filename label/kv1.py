from kivymd.app import MDApp
from kivy.lang import Builder

kv = '''
Screen:
    BoxLayout:
        orientation:"vertical"
    MDToolbar:
        title: "AtmegaRobotics"
    MDLabel:
        text:"AR"
        halign:"center"
'''

class demo(MDApp):
    def build(self):
        return Builder.load_string(kv);
demo().run();