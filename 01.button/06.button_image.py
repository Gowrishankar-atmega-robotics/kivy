from kivymd.app import MDApp 
from kivy.uix.button import Button 
class demo(MDApp):
    def build(self):
        but = Button(background_normal = '/home/atmegarobotics/Desktop/kivy/3.jpg',size =(10 , 10) , size_hint=(.1 , .1), pos =(350, 250) );
        return but ;

demo().run();