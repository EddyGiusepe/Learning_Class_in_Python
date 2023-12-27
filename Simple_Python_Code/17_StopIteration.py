#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

StopIteration
=============
A seguir usamos StopIterationinstrução. No método __next__(), podemos
adicionar uma condição de terminação para gerar um erro se a iteração
for feita um determinado número de vezes.
"""

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self 
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a = self.a + 1
            return x
        else:
            raise StopIteration
        


if __name__ == '__main__':
    minha_class = MyNumbers()
    minha_Iter = iter(minha_class)

    for i in minha_Iter:
        print(i)
