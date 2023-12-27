#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

The self parameter
==================
O parâmetro 'self' é uma referência à instância atual da classe e é usado para acessar
variáveis ​​que pertencem à classe. Não precisa ter nome 'self', você pode chamá-lo como
quiser, mas tem que ser o primeiro parâmetro de qualquer função da classe. Neste script
mostramos isso.
"""

class Person:
    def __init__(eddy_self1, name: str, age: int):
        eddy_self1.name = name
        eddy_self1.age = age

    def myfunction(eddy_self2):
        print("Olá, meu nome é " + eddy_self2.name + " e a minha idade é " + str(eddy_self2.age) + " anos.")



if __name__ == '__main__':
    ins_class = Person("Eddy", 42)
    ins_class.myfunction()
