#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Group Anagrams
==============
Dado um array de strings strs, agrupe os anagramas. Você pode retornar a resposta em qualquer ordem.

Um Anagrama é uma palavra ou frase formada pela reorganização das letras de uma palavra
ou frase diferente, normalmente usando todas as letras originais exatamente uma vez.
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            anagrams_dict[key].append(s)

        return anagrams_dict.values()
          
    


if __name__ == '__main__':
    solution_Eddy = Solution()
    strs = ["eat", "tan", "tea", "nat"]
    resultado_str = solution_Eddy.groupAnagrams(strs=strs)
    print("Vejamos os Anagrams: ", resultado_str)
