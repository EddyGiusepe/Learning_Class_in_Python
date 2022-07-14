import datetime

class Entrevista():
    nome = ""
    ano_informado = 0
    idade = 0

    def pergunta_nome(self):
        self.nome = input("Qual é o seu nome (Digite FIM para encerrar)? ")
        print("O seu nome é '" + self.nome + "'")
        return self.nome

    def pergunta_idade(self):
        ano_atual = datetime.date.today().year
        # Pergunta em que ano você nasceu
        self.ano_informado = int(input("Ola " + self.nome + ", qual é seu ano de nascimento"))
        # Subtrair o ano atual do ano informado
        self.idade = ano_atual - self.ano_informado
        # Imprimir na tela a idade Calculada
        print("Você tem", self.idade, " anos.")

        # Return (self.ano_informado, self.idade) # tuple  - tupla

        def __str__(self):
            return "{}/{}".format(self.nome, self.idade)

        def __repr__(self):
            return "Nome = {} - Idade = {}".format(self.nome, self.idade)








