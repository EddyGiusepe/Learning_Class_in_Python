'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro

Link de estudo --> https://www.youtube.com/watch?v=WP5p4QEqLLQ&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=1
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



print("==========================")
print("Exemplo do controle remoto")
print("==========================")
class ControleRemoto():

    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print('Canal avançado')

    def voltar_canal(self):
        print('Voltar canal')

    def escolher_canal(self, canal):
        print("Alterado para o canal: {}".format(canal))

# Na sala:
controle_sala = ControleRemoto('samsung', 'sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)

print("")
# No quarto
controle_quarto = ControleRemoto('LG', 'quarto')
print(controle_quarto.comodo)
print(controle_quarto.televisao)

















