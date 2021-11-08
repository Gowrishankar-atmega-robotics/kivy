from kivy.lang import Builder 
from kivymd.app import MDApp 
kv = '''
MDRaisedButton:
    text: "Atmega"
    pos : (300,500)
    md_bg_color:1,0,0,1
'''
class demo(MDApp):
    def build(self):
        return Builder.load_string(kv);
demo().run();
