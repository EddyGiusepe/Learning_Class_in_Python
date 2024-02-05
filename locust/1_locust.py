#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Execução:

$ locust -f 1_locust.py
ou
$ locust -f 1_locust.py --modern-ui
"""
from locust import HttpUser, task, constant, constant_throughput, constant_pacing, between
import random
from locust import TaskSet

# class UsuarioQAEstresse(HttpUser):
#     #wait_time = between(1 , 5)
#     #wait_time = constant_throughput(10) # Me dá RPS=21. This is the mathematical inverse of constant_pacing.
#     wait_time = constant_pacing(0.1)
#     #wait_time = constant(0.1)  # Tempo de espera entre as solicitações em segundos (Usado no 'task').

#     @task
#     def enviar_pergunta(self):


#         # # Enviando a query a nossa aplicação:
#         r = self.client.get("http://0.0.0.0:8000/") # "https://google.com"
#         print(r.status_code)



class MyTaskSet(TaskSet):

    @task
    def my_task(self):
        r = self.client.get("http://0.0.0.0:8000/")
        print(r.status_code) 



class MyUser(HttpUser):
    tasks = [MyTaskSet]
    wait_time = constant(10)  # Tempo entre as execuções das tarefas
    # min_wait = 0
    # max_wait = 0
