"""
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro
Link de estudo: http://pythonclub.com.br/introducao-classes-metodos-python-basico.html
"""
class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def multiplica(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a/self.b

# if __name__ == "__main__":
print("Instanciamos os objetos: ")
dois_numeros = Calculadora(4, 0)
sum = dois_numeros.soma()
rest = dois_numeros.subtrai()
div = dois_numeros.divide()
print(sum)
print(rest)
print(div)




