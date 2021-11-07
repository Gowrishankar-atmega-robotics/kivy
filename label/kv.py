from kivy.lang import Builder
from kivymd.app import MDApp


kv = '''
Screen:
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "MDLabel1"
            
        MDLabel:
            text: "MDLabel2"
'''

class demo(MDApp):
    def build(self):
        return Builder.load_string(kv);
demo().run();
