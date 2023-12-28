#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Class Polymorphism
==================
O polimorfismo é frequentemente usado em métodos de classe, onde podemos
ter várias classes com o mesmo nome do método. Por exemplo, digamos que temos três
classes: Carro, Bote e Aviao, e todas elas têm um método chamado move():
"""

# Classes diferentes com o mesmo método:
class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def movimento(self):
        print("Conduzir!")


class Bote:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def movimento(self):
        print("Navegar!")


class Aviao:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def movimento(self):
        print("Voar!")




if __name__ == "__main__":
    carro_1 = Carro("Ford", "Mustang")
    bote_1 = Bote("Ibiza", "Touring 20")
    aviao_1 = Aviao("Boeing", "747")


    for x in (carro_1, bote_1, aviao_1):
        x.movimento()
