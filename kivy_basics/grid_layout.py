from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
class Mainapp(App):
    def build(self):
        layout=GridLayout(cols=2,row_force_default=True,row_default_height=40)#based on columns mentioned rows will be created accoring to the data
        btn1=Button(text="Hello1",size_hint=(None,None),width=100,height=40)
        btn2=Button(text="World1")
        btn3=Button(text="Hello2",size_hint=(None,None),width=100,height=40)
        btn4=Button(text="World2")
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        return layout

Mainapp().run()