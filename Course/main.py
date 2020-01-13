#encoding: utf-8

from kivy.app import App
from kivy.uix.label import Label

def build():
    return Label(text = 'Hello World')

hello_world = App()
hello_world.build = build       # Overriding App().build method?
hello_world.run()

'''
Ref to make run()  work: https://stackoverflow.com/questions/40697876/unable-to-get-a-window-abort
pip install --upgrade pip wheel setuptools
pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
pip install kivy.deps.gstreamer
pip install kivy.deps.angle
pip install kivy

'''