#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Este estudo sobre Classes foi baseado no Tutorial do "Greg Hogg".
Dado um array inteiro nums, retorne todos os trigêmeos
"""
from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ret = set()
        d = {}
        n = len(nums)

        for i, num in enumerate(nums):
            d[num] = i

        for i in range(n):
            for j in range(i + 1, n):
                z = -(nums[i] + nums[j])
                if z in d and d[z] != i and d[z] != j:
                    triple = sorted([nums[i], nums[j], z])
                    triple = tuple(triple)
                    ret.add(triple)

        return ret                
          
    


if __name__ == '__main__':
    solution_Eddy = Solution()
    nums = [3, 6, 4, -1, -2]
    resultado = solution_Eddy.threeSum(nums=nums)
    print("Vejamos a resposta: ", resultado)
