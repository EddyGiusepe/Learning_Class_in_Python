'''
 https://docs.python.org/3/library/
https://www.youtube.com/watch?v=5-qU3rsKZz4
'''

import meumodulo

parar_repeticao = False
lista_de_entrevistados = []

while parar_repeticao == False:
    entrevistado = meumodulo.Entrevista() # Instância da classe
    if entrevistado.pergunta_nome() == 'fim':
        parar_repeticao = True
    else:
        entrevistado.pergunta_idade()
        lista_de_entrevistados.append(entrevistado)

print(lista_de_entrevistados)

for entr in lista_de_entrevistados:
    print("Nome = {} | Ano Nascimento = {}".format(
        entr.nome,
        entr.ano_informado
        )
    )
