from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.label import Label 
class demo(App):
    def build(self):
        bt = Button(text="click here", font_size="18sp",size_hint=(0.1,0.1),pos=(500, 300));
        bt.bind(on_press = self.fun)
        return bt
    def fun(self , event):
        lb = Label(text="heelo",halign = "center")
        return lb

demo().run()
            
