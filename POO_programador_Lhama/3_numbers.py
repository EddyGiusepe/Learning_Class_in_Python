#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
def plusMinus(arr):
    # Obtendo o tamanho do array
    n = len(arr)
    
    # Inicializando contadores para positivos, negativos e zeros
    positivos = 0
    negativos = 0
    zeros = 0
    
    # Iterando pelo array para contar os números
    for num in arr:
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
        else:
            zeros += 1
    
    # Calculando as proporções
    proporcao_positivos = positivos / n
    proporcao_negativos = negativos / n
    proporcao_zeros = zeros / n

    # Imprimindo as proporções com 6 casas decimais
    print("{:.6f}".format(proporcao_positivos))
    print("{:.6f}".format(proporcao_negativos))
    print("{:.6f}".format(proporcao_zeros))

if __name__ == '__main__':
    n1 = input("Ingressa o números: ").strip()

    arr = list(map(int, n1.split()))

    plusMinus(arr)
