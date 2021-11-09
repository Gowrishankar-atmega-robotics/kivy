import os
os.environ["KIVY_TEXT"] = "pil"

from kivy.lang import Builder 
from kivymd.app import MDApp 
#from kivy.uix import label
#print(dir(label))
kv = '''
MDScreen:
    MDFloatingActionButtonSpeedDial:
        data : app.data 
        root_button_anim: True
'''
class demo(MDApp):
    data = {
        'Python': 'language-python',
        'PHP' : 'language-php'
    }
    def build(self):
        build = Builder.load_string(kv);
        return build 
demo().run();