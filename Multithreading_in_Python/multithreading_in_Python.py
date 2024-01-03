#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro


O que é multithreading?
=======================
Multithreading é uma técnica de programação que permite que um programa
execute vários threads (unidades menores de um programa) simultaneamente
dentro do mesmo processo. Cada thread é executado de forma independente
e pode realizar suas próprias tarefas, proporcionando a ilusão de paralelismo.

Em python, o multithreading pode ser alcançado usando o módulo Threading.
Este módulo fornece classes e funções para criar e gerenciar threads.

Python também fornece a classe 'concurrent.futures.ThreadPoolExecutor', que
simplifica o gerenciamento de um conjunto de threads para execução simultânea
de funções. Sintaxe:

                    import threading

                    def my_function(value):
                        # Código a ser executado no thread.
                        pass 
                    # Crie um objeto de thread:
                    my_thread = threading.Thread(target=my_function, args=value)

                    # Inicie a thread:
                    my_thread.start()

                    # Espere o thread finalizar:
                    my_thread.join()
"""

"""
Explanação
----------
* O método start() inicia a execução dos threads. Isso significa que
  "print_numbers" e "print_letters" serão executados simultaneamente em
  threads separados.

* Costuma-se dizer que os 'threads' são executados ao mesmo tempo, mas
  na verdade eles estão sendo executados consecutivamente em intervalos
  de tempo alocados para os threads. Você pode ver na saída.

* O método join() bloqueia o thread principal (aquele que iniciou os dois threads)
  até que thread1 e thread2 terminem a execução.

* Isso garante que o thread principal não seja encerrado prematuramente e
  aguarde que os dois threads concluam seu trabalho.

Por que Usar?
-------------
* Simultaneidade (Concurrency): Multithreading permite executar múltiplas tarefas simultaneamente,
                                o que pode melhorar a capacidade de resposta do seu programa.

* Tarefas vinculadas a E/S (I/O-Bound Tasks): É particularmente útil para tarefas E/S-bound, onde
  os threads podem executar operações que não exigem muita CPU, como ler/gravar arquivos, fazer
  solicitações de rede ou aguardar a entrada do usuário. Threads podem ceder controle ao aguardar E/S (I/O),
  permitindo que outros threads sejam executados.     
  
"""
import threading
import time

# Criamos uma função para printar números:
def print_numbers():
    for i in range(1, 6):
        print(f"🦆🦆 Imprimir o número chamado: {i}")
        time.sleep(1)

# Criamos uma função para printar letras:
def print_letters():
    for j in 'abcde':
        print(f"🤗🤗 Imprimir a letra chamada: {j}")
        time.sleep(4)

# Criamos dois objetos thread:
thread_1 = threading.Thread(target=print_numbers)
thread_2 = threading.Thread(target=print_letters)

# Iniciamos os thread:
thread_1.start()
thread_2.start()

# Esperamos os thread finalizar:
thread_1.join()
thread_2.join()
print("Os dois threads terminaram")
