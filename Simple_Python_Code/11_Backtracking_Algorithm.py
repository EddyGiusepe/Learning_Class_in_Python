#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""

def subsets(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    path = []
    res = []

    def backtrack(i: int):
        if i == n:
            res.append(path.copy())
            return
        
        next_number = nums[i]

        # Don't use number:
        backtrack(i + 1)

        # Use number:
        path.append(next_number)
        backtrack(i + 1)
        path.pop()

        return res

    return backtrack(0)




if __name__ == '__main__':
    array = [3, 1, 2] # Resposta será: [[], [2], [1], [1, 2], [3], [3, 2], [3, 1], [3, 1, 2]]
    response = subsets(array)
    print(response)
