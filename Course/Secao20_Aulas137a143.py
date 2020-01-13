#coding: utf-8

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

''' Ref to make run() work: https://stackoverflow.com/questions/40697876/unable-to-get-a-window-abort
pip install --upgrade pip wheel setuptools
pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
pip install kivy.deps.gstreamer
pip install kivy.deps.angle
pip install kivy

'''

#def build():
#    lb = Label()
#    lb.text = 'Hello World'
#    lb.italic = True
#    lb.font_size = 50
#    return lb

def click():
    print(txtInput.text)
    return

def build():
    layout = FloatLayout()
    
    global txtInput
    txtInput = TextInput()
    txtInput.text = 'Digite algo: '
    txtInput.size_hint = None, None # Resizing to default.
    txtInput.height = 400
    txtInput.width = 400
    txtInput.x = 100                # Distância da margem esquerda.
    txtInput.y = 150                # Distância da base do video.

    bt = Button()
    bt.text = 'Clique aqui'
    bt.size_hint = None, None # Resizing to default.
    bt.height = 50
    bt.width = 200

    bt.x = 200                  # Distância da margem esquerda.
    bt.y = 75                   # Distância da base do video.
    bt.on_press = click

    layout.add_widget(txtInput)
    layout.add_widget(bt)

    return layout




app = App()
app.title = "eXcript"
Window.size = 600,600
app.build = build       # Overrides App().build() method?
app.run()

