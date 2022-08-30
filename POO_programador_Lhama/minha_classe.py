'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
print("=========")
print("Exemplo 1")
print("=========")

class MinhaClasse:

    def meu_metodo(self):
        print("Estou no método!")

# Instanciando minha classe:
objeto = MinhaClasse()
objeto.meu_metodo()


print("=========")
print("Exemplo 2")
print("=========")

class MinhaClasse:

    def meu_metodo(self):
        print("Estou no método!")

    def meu_metodo2(self, num, mult):
        return num * mult


# Instanciando minha classe:
objeto = MinhaClasse()
result = objeto.meu_metodo2(3, 2)
print(result)


print("=========")
print("Exemplo 3")
print("=========")

class MinhaClasse:

    def __init__(self, att):
        self.meu_atributo = 'Olá Mundo'
        self.meu_atributo2= att

    def meu_metodo(self):
        print("Estou no método!")

    def meu_metodo2(self, num, mult):
        return num * mult


# Instanciando minha classe:
objeto = MinhaClasse('meu_atributo')
print(objeto.meu_atributo)


print("=========")
print("Exemplo 4")
print("=========")

class MinhaClasse:

    def __init__(self, att):
        self.meu_atributo = 'Olá Mundo'
        self.meu_atributo2= att

    def meu_metodo(self):
        print(self.meu_atributo)
        print(self.meu_atributo2)

    def meu_metodo2(self, num, mult):
        return num * mult


# Instanciando minha classe:
objeto = MinhaClasse(23)
objeto.meu_metodo()