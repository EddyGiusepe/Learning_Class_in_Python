#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Substring mais longa sem caracteres repetidos
=============================================
Dada uma string s, encontre o comprimento da substring mais longa sem repetir caracteres.
"""
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s):
        l = 0
        sett = set()
        max_len = 0

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            sett.add(s[r])
            max_len = max(max_len, r - l + 1)        

        return max_len
          
    


if __name__ == '__main__':
    solution_Eddy = Solution()
    string = "abcabbbmnpq"
    resultado = solution_Eddy.lengthOfLongestSubstring(s=string)
    print("Vejamos a resposta: ", resultado)
