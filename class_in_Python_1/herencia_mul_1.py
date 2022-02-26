'''
Link de estudo: https://www.youtube.com/watch?v=E76ErVQ1xNI&list=PLqlQ2-9ypflT5Lx864RXtJx4s7i3sxgs0&index=17
'''

class A:
    def __init__(self):
        print("Sou da classe A")
    def a(self):
        print("Este método foi heredado de A")

class B():
    def __init__(self):
        print("Sou da classe B")
    def b(self):
       print("Este método foi heredado de B")
# Aqui a classe C hereda tudo da classe A e B
class C(B, A):
    def c(self):
       print("Este método é de C")

if __name__ == "__main__":
    x = C()
    x.c()
    x.b()
    x.a()
    print("Usamos dois métodos para fazer as seguintes perguntas: ")
    print(issubclass(C, B)) # C é uma subclass de B ?
    print(issubclass(B, C))  # B é uma subclass de C ?
    print("")
    print(isinstance(x, C))  # x é uma instância de C ?