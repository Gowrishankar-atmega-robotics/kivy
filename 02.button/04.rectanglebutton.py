from kivymd.app import MDApp
from kivymd.uix.screen import Screen 
from kivymd.uix.button import MDRectangleFlatButton 

class demo(MDApp):
    def build(self):
        screen = Screen()
        bt = MDRectangleFlatButton(text="click here",pos=(500,300),on_release = self.fn);
        screen.add_widget(bt);
        return screen 
    def fn(self, event):
        print("AR");
demo().run();