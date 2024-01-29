#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
import math
import os
import random
import re
import sys

def miniMaxSum(arr: list[int]) -> int:
    # Ordeno os números de forma crescente:
    arr.sort()

    # Calculo a soma Mínima:
    soma_minima = sum(arr[:4])

    # Calculo a soma Máxima:
    soma_maxima = sum(arr[1:])
    
    return soma_minima, soma_maxima
       


if __name__ == '__main__':
    entrada = input("Escreva APENAS os 5 números separados por espaço: ")
    arr = list(map(int, entrada.split()))
    
    minimo, maximo = miniMaxSum(arr)
    
    print(minimo, maximo)
