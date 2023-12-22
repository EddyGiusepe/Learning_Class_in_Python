#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""


class Car:
    def __init__(self, modelo, marca, ano):
        self.__details__ = {
            "modelo": modelo,
            "marca": marca,
            "ano": ano
        }

    def get_marca(self):
        return self.__details__["marca"]
    

if __name__ == '__main__':
    garagem = [Car("Modelo S", "Tesla", 2020), Car("Corolla", "Toyota", 2019)]
    resposta = garagem[0].get_marca()
    print(resposta)
    