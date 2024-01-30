#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
def findMedian(arr):
    lista_ordenada = sorted(arr)
    indice_med = len(lista_ordenada) // 2
    
    return lista_ordenada[indice_med]
    

if __name__ == '__main__':
    entrada = input("Igresa os números da sua lista, separados por espaço (Quantidade ímpar): ")
    lista = list(map(int, entrada.split()))
    
    mediana = findMedian(lista)
    print(f"A Mediana da lista é: {mediana}")