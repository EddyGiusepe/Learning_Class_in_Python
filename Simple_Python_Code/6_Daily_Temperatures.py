#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Daily Temperatures
==================
Este estudo sobre Classes foi baseado no Tutorial do "Greg Hogg".

Dada uma matriz de números inteiros, Temperatures representa as 
temperaturas diárias, retorne uma resposta de matriz tal que 
resposta[i] seja o número de dias que você terá que esperar 
após o dia 'ith' para obter uma temperatura mais quente. Se 
não houver nenhum dia futuro para o qual isso seja possível, 
mantenha answer[i] == 0.
"""
from collections import defaultdict

class Solution:
    def dailyTemperatures(self, temps: list[int]) -> list[int]:
        answer = [0] * len(temps)
        stk = []

        for i in range(len(temps)):
            while stk and stk[-1][1] < temps[i]:
                stk_i, stk_temp = stk.pop()
                answer[stk_i] = i - stk_i


            stk.append((i, temps[i]))

        return answer        

          
    


if __name__ == '__main__':
    solution_Eddy = Solution()
    temperatures = [72, 70, 81, 91] #[73, 74, 75, 71, 69, 72, 76, 73]
    resultado = solution_Eddy.dailyTemperatures(temps=temperatures)
    print("Vejamos a resposta: ", resultado)
