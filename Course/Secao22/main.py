#coding: utf-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout




class RootWidget(FloatLayout):
    pass


class HelloApp(App):   
    ''' Python reconhece arquivo kv automaticamente se:
    Estiver na mesma pasta.
    Nome do arquivo kv:
        Com letra minúscula
        Sem "App"
    Ex: HelloApp(App) -> hello.kv
    Nome da classe:
        Não precisa conter "App"
        Não precisa conter letras maiúsculas.'''

    def build(self):
        return RootWidget()
    pass


HelloApp().run()
''' Ref to make run() work: https://stackoverflow.com/questions/40697876/unable-to-get-a-window-abort
pip install --upgrade pip wheel setuptools
pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
pip install kivy.deps.gstreamer
pip install kivy.deps.angle
pip install kivy

'''