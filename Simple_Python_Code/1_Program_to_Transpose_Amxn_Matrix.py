"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Neste script calculamos a Transposta de uma matriz.
"""

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in m:
    print(row)

trns = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

print("\n")
for row in trns:
    print(row)
