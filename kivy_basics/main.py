from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)


class Mainapp(App):
    def build(self):
        label = Label(text="Hello world!!", font_size="20 sp", bold=True, italic=True,color=(0,0,0,1))
        return label


Mainapp().run()
