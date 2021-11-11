from kivy.lang import Builder 
from kivymd.app import MDApp 

kv = '''
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None 
MDFloatLayout:
    Check:
        active : True
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        
'''
class demo(MDApp):
    def build(self):
        return Builder.load_string(kv)
demo().run();
