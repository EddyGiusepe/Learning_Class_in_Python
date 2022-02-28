class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


print("Instanciamos dois objetos: ")
nome_1 = Pessoa("Eddy")
print(nome_1)
nome_2 = Pessoa("Karina")
print("O nome da minha esposa é: {}".format(nome_2))


