"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Contains Duplicate
==================
Dado um array de números inteiros, retorne 'verdadeiro' se algum valor aparecer
pelo menos duas vezes no array e retorne 'falso' se cada elemento for distinto.
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        h = set()

        for num in nums:
            if num in h:
                return True
            else:
                h.add(num)
            
        return False
    


if __name__ == '__main__':
    solution_Eddy = Solution()
    nums = [1, 5, 5, 6, 8, 8, 9]
    resultado_lista = solution_Eddy.containsDuplicate(nums=nums)
    print("Se a nossa lista contém números repetidos é True, senão é False: ", resultado_lista)
