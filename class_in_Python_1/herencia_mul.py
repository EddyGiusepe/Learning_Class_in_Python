class A:
    def __init__(self):
        print("Sou da classe A")
    def a(self):
        print("Este método foi heredado de A")

class B(A):
    def __init__(self):
        print("Sou da classe B")
    def b(self):
       print("Este método foi heredado de B")

class C(B):
    def c(self):
       print("Este método é de C")

if __name__ == "__main__":
    x = C()
    x.c()
    x.b()
    x.a()