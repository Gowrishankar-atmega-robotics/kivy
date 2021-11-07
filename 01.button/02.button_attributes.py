from kivy.app import App
from kivy.uix.button import Button

class demo(App):
    def build(self):
        return Button(text="click me",color=(0.4,0.5 , 0.6 , 0.7),background_color=(1,0,0,1),size_hint=(.2, .1), pos=(500,300))
demo().run()
