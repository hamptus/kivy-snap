#!/usr/bin/env python3

import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput

from kivy.config import Config
Config.set('kivy', 'log_level', 'debug')

class KivySnapApp(App):

    def build(self):
        return TextInput()

if __name__ == '__main__':
    KivySnapApp().run()