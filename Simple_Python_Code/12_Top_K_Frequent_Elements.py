#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Top_K Frequent Elements
=======================
Dado um array inteiro nums e um inteiro k, retorne os k elementos mais frequentes.
Você pode retornar a resposta em qualquer ordem.
"""
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        counter = Counter(nums)
        buckets = [0] * (n + 1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num) 

        ret = [] 
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break

        return ret # Time O(n)            


if __name__ == '__main__':
    minhaClass = Solution()
    nums = [1, 2, 3, 3, 3, 2, 4, 5, 5, 5]
    k = 2
    resposta = minhaClass.topKFrequent(nums=nums, k=k)
    print(resposta)
    