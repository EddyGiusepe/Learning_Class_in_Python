#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Validando o Cartão de Crédito
=============================
Neste exemplo simples de cartão de crédito
a quantidade de números que deve ter o cartão de crédito
é 20.

Execução:

$ python 2_credit_Card_Validation.py
"""

def validate(card_number: int) -> int:
    '''Função principal que recebe um número de cartão de
       crédito como entrada e retorna um valor que indica
       se o número do cartão é válido ou não.'''

    def digits_of(n):
        '''Função auxiliar para extrair os dígitos de um número'''
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)

    # Obtém os dígitos nas posições ímpares e pares:
    odd_digits = digits[-1::-2] # Dígitos nas posições ímpares
    even_digits = digits[-2::-2] # Dígitos nas posições pares
    
    checksum = 0
    # Soma os dígitos nas posições ímpares
    checksum += sum(odd_digits)
    
    # Itera sobre os dígitos nas posições pares:
    for d in even_digits:
        checksum += sum(digits_of(d*2))

    return checksum % 10


if validate(input("Digita teu número de Cartão de Crédito: \n")) == 0:
    print("Valido")

else:
    print("Invalido")




