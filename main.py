#!/usr/bin/env python3

import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput

from kivy.config import Config
from kivy.core.window import Window

Config.set('kivy', 'log_level', 'debug')

class KivySnapApp(App):

    def build(self):
        return TextInput()

if __name__ == '__main__':
    def print_event(*args, **kwargs):
        print(args)
        print(kwargs)

    app = KivySnapApp()
    Window.bind(on_keyboard=print_event)
    app.run()