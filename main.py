from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivy.uix.button import ButtonBehavior,Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager,Screen,NoTransition,CardTransition
from kivy.config import Config



Config.set('graphics', 'width', '1100')
Config.set('graphics', 'height', '750')
Config.set('graphics', 'borderless', '1')
Config.write()

class ImageButton(ButtonBehavior,Image):
    pass

class LabelButton(ButtonBehavior,Label):
    pass

class Spacer(Label):
    pass

class DashboardScreen(Screen):
    pass

GUI = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return GUI

    def on_start(self):
        LabelBase.register(name= 'myraid_pro_reg', fn_regular ='MYRIADPRO-REGULAR.OTF')
        LabelBase.register (name='d_ding_reg', fn_regular='d-din.regular.ttf')
        LabelBase.register (name='roboto-medium', fn_regular='Roboto-Medium.ttf')
        LabelBase.register (name='roboto-thin', fn_regular='Roboto-Thin.ttf')
        LabelBase.register (name='bistecca', fn_regular='Bistecca.ttf')
        LabelBase.register (name='teko-reg', fn_regular='Teko-Regular.ttf')
        LabelBase.register (name='barlow-reg', fn_regular='BarlowSemiCondensed-Regular.ttf')
        LabelBase.register (name='barlow-bold', fn_regular='BarlowSemiCondensed-SemiBold.ttf')

    def close(self):
        quit()

    def minimize(self):
        Window.minimize()

MainApp().run()

