#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""

import periodictable

def get_element_info(symbol: str):
    """Função verifica se o Símbolo é valido"""

    try: 
        # Acessando a informações específicas do Elemento:
        element = periodictable.elements.symbol(symbol)

        # Printamos as informações:
        print(f"Nome do Elemento químico: {element.name}")
        print(f"Símbolo químico: {element.symbol}")
        print(f"Número Atômico: {element.number}")
        print(f"Peso Atômico: {element.mass}")
        print(f"Densidade: {element.density}")
    
    except ValueError:
        print("Símbolo químico invalido")
        


# Prompt do usuário para ingressar o símbolo químico:
element_symbol = input("Digita o símbolo do Elemento Químico: ")

# Chamamos a nossa função:
get_element_info(element_symbol)
