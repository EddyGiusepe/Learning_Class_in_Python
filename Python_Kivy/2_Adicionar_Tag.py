#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
from kivy.app import App
from kivy.uix.label import Label

class MyLabelApp(App):
    def build(self):
        texto = input("Digite seu texto: ")
        rotulo = Label(text=texto,
                       font_size="20 sp", # Unidade de medida --> scaled pixels
                       color="#DF7848") # color: "green" ou "#6ADF48" (em sistema Hexadecimal)
        return rotulo




if __name__ == '__main__':
    kivy = MyLabelApp()
    kivy.run()