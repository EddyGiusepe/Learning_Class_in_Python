#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Kivy
====
Neste script fazemos uma introdução à biblioteca Kivy em Python.
Esta biblioteca serve para desenvolver aplicativos desktops. 
"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class HelloWorld(App):
    def build(self):
        Label(text="Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro")
        #return Button(text='Olá, Kivy!') # Para fazer click na tela
        return Label(text='Olá, Kivy!') # Para observar apenas o texto



#HelloWorld().run()

if __name__ == '__main__':
    kivy = HelloWorld()
    kivy.run()