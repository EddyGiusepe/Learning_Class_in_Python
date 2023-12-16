#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Two Sum II: A matriz de entrada é Sorted
========================================

Dada uma matriz 1-indexed de números inteiros que já está sorted em
ordem não decrescente, encontre dois números de forma que eles somem
um número de destino específico. Sejam esses dois números números[índice1]
e números[índice2] onde 1 <= índice1 <índice2 <números.legth.
"""
class Solution:
    def twoSum(self, numbers: list[int], target: int):

        L = 0
        R = len(numbers) - 1

        while L < R:
            summ = numbers[L] + numbers[R]

            if summ > target:
                R -= 1
            elif summ == target:
                return L + 1, R + 1
            else:
                L += 1    


          
    


if __name__ == '__main__':
    solution_Eddy = Solution()
    numbers = [2, 7, 11, 15] # Para nosso problema a posição considerada é: 1; 2; 3; . . .
    print(numbers[1])
    target = 18
    resultado = solution_Eddy.twoSum(numbers=numbers, target=target)
    print("Vejamos a resposta: ", resultado)
