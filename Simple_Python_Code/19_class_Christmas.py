#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
class Natal:
    def __init__(self, tradicao: str, pais: str):
        self.__details = {
            'tradicao': tradicao,
            'pais': pais
        } 

    def obter_tradicao(self):
        return self.__details['tradicao']


if __name__ == '__main__':
    celebracao = [Natal("Decorar a árvore de Natal", "USA"), Natal("Tomar chocolate caliente a la media noche con Paneton", "Perú")]
    resposta = celebracao[0].obter_tradicao() 
    print(resposta)
    