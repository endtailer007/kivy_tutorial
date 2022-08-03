from kivy.app import App
from kivy.uix.image import Image,AsyncImage

class Mainapp(App):
    def build(self):
        #img=Image(source='merc.png')
        img=AsyncImage(source='https://w7.pngwing.com/pngs/38/708/png-transparent-car-mercedes-car-love-compact-car-vehicle-thumbnail.png')
        return img

Mainapp().run()