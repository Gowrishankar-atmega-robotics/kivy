from kivy.lang import Builder 
from kivymd.app import MDApp 

kv = """
Screen:
    MDDropDownItem:
        id: drop_item 
        pos_hint: {'center_x':0.5 , 'center_y': 0.5} 
        text : "Item"
        on_release: self.set_item("New Item")
"""
class demo(MDApp):
    def __init__(self, **kwargs):
        super().__init__( **kwargs )
        self.screen = Builder.load_string(kv);
    def build(self):
        return self.screen 
demo().run()
