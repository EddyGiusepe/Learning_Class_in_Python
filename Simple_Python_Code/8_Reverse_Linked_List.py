#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Reverse Linked List
===================
Dado o cabeçalho de uma lista vinculada individualmente, inverta a lista e retorne a lista invertida.
"""
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"ListNode({self.value})"

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

# Criando uma lista encadeada para teste:
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

# Criando uma instância da classe Solution:
solution = Solution()

# Chamando o método reverseList e armazenando o resultado em reversed_head:
reversed_head = solution.reverseList(node1)

# Imprimindo os valores da lista invertida
while reversed_head:
    print(reversed_head)
    reversed_head = reversed_head.next

# if __name__ == '__main__':
#     solution_Eddy = Solution()
#     head = ListNode(1, ListNode(2, ListNode(3)))
#     resultado = solution_Eddy.reverseList(head=head)
#     print("Vejamos a resposta: ", resultado)
