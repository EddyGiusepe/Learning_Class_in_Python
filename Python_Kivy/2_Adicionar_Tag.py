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
                       font_size="80 sp", # Unidade de medida --> scaled pixels
                       color="green") 
        return rotulo




if __name__ == '__main__':
    kivy = MyLabelApp()
    kivy.run()