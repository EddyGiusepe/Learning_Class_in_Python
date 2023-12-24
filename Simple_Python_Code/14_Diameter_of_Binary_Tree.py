#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Diameter of Binary Tree
=======================
Dada a raiz de uma árvore binária, retorne o comprimento do diâmetro da árvore.
O diâmetro de uma árvore binária é o comprimento do caminho mais longo entre quaisquer
dois nós de uma árvore. Este caminho pode ou não passar pela raiz. O comprimento do
caminho entre dois nós é representado pelo número de arestas entre eles.

"""

class Solution:
    def diameterOfBinaryTree(self, root):
        maxx = [0]

        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)
            maxx[0] = max(maxx[0], left + right)

            return 1 + max(left, right)

        dfs(root)
        return maxx[0]
    

if __name__ == '__main__':
    solution_Eddy = Solution()
    root = [1, 2, 3, 4, 5]
    resultado = solution_Eddy.diameterOfBinaryTree(root=root)
    print("Vejamos a resposta: ", resultado)