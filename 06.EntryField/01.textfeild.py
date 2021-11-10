from kivymd.app import MDApp 
from kivymd.uix.screen import Screen 
from kivymd.uix.textfield import MDTextField 

class demo(MDApp):
    def nit(self):
        val = input("enter the text you want to see: " , )
        return val 
    def build(self):
        scr = Screen();
        v = demo();
        c = v.nit()
        tf = MDTextField(text = c ,pos_hint = {"center_x" : 0.5, "center_y":0.5},size_hint=(0.5,1));
        scr.add_widget(tf)
        return scr 
demo().run();