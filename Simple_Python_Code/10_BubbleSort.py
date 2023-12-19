#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""

def bubbleSort(array):
    made_a_swap = True
    n = len(array)

    while made_a_swap:
        made_a_swap = False

        for i in range(n - 1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                made_a_swap = True

    return array                




if __name__ == '__main__':
    array = [5, 3, 1, 2] # Resposta será: [1, 2, 3, 5]
    response = bubbleSort(array=array)
    print(response)
