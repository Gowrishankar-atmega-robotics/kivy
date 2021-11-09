#from kivymd.uix.button import MDFlatButton  
#print(dir(MDFlatButton)); 
from kivy.app import App
from kivy.uix.layout import Layout
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy_garden.mapview import MapView , MapMarker
import cv2

class CamApp(App):
    

    def build(self):
        
        self.img1=Image()
        self.img1.pos=(-500, 200)
        layout = RelativeLayout()
        #layout.size_hint=(.5 , .5)
        mapv = MapView(zoom = 11, lat =10.117342231510762, lon = 76.35389246135595,size_hint=(0.5, 0.5),pos=(500, 300))
        layout.add_widget(self.img1 )
        layout.add_widget(mapv)
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        self.capture.set(4, 480);
        self.capture.set(3, 320);
        cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout 

    def update(self, dt):
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        cv2.imshow("CV2 Image", frame)
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
        #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer. 
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1

        

if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()

