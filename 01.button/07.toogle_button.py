from kivy.app import App 
from kivy.uix.togglebutton import ToggleButton 
from kivy.uix.floatlayout import FloatLayout 
from kivymd.app import MDApp 
from kivymd.uix.screen import Screen 
class demo(App):
    def build(self):
        scr = Screen()
        click = ToggleButton(text ="click here", size_hint=(0.1,0.1), pos=(350, 300), font_size = "12");
        tb = ToggleButton(background_normal = "3.jpg",size_hint=(.2,.2))
        scr.add_widget(click);
        scr.add_widget(tb);
        return scr ; 
demo().run();