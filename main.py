#!/usr/bin/env python3

import os
os.environ['KIVY_WINDOW'] = os.environ['KIVY_TEXT'] = 'sdl2'

import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput

from kivy.config import Config
from kivy.core.window import Window

Config.set('kivy', 'log_level', 'debug')

class TI(TextInput):

    def _key_down(self, key, repeat=False):
        print("KEY DOWN")
        print(key)
        super(TI, self)._key_down(key, repeat)

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        print("KEYBOARD_ON_KEY_DOWN")
        print(window, keycode, text, modifiers)
        super(TI, self).keyboard_on_key_down(window, keycode, text, modifiers)

    def keyboard_on_textinput(self, window, text):
        print("KEYBOARD_ON_TEXTINPUT")
        print(window, text)
        if self._selection:
            self.delete_selection()
        self.insert_text(text, False)

class KivySnapApp(App):

    def build(self):
        return TI()

if __name__ == '__main__':
    def print_event(*args, **kwargs):
        print(args)
        print(kwargs)

    app = KivySnapApp()
    Window.bind(on_keyboard=print_event)
    app.run()
