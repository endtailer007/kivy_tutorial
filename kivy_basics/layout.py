# Box and grid layouts
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage

Window.clearcolor = (1, 1, 1, 1)
Window.size = (360, 600)


class Mainapp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing='150 sp', padding='80 sp')  # vertical arrangement of elements
        image = Image(source='merc.png')
        button = Button(text='Login', size_hint=(None, None), width=150, height=50, pos_hint={'center_x': 0.5})
        layout.add_widget(image)
        layout.add_widget(button)
        return layout


Mainapp().run()
