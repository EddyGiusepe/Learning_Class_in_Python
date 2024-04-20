#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
class Chatbot:
    def __init__(self):
        self.perguntas_respostas = {
            "olá": "Olá! Como você está?",
            "tchau": "Tchau! Até mais!",
            "como você está": "Estou bem, obrigado!",
            "quem é você": "Sou um Chatbot simples criado em Python!",
            "ajuda": "Posso ajudar com perguntas básicas. Tente me perguntar algo!"
        }

    def responder(self, pergunta):
        pergunta = pergunta.lower()  # converter para minúscula
        if pergunta in self.perguntas_respostas:
            return self.perguntas_respostas[pergunta]
        else:
            return "Desculpe, não entendi. Tente novamente!"

    def iniciar_conversa(self):
        print("Bem-vindo ao Chatbot!")
        while True:
            pergunta = input("Você: ")
            resposta = self.responder(pergunta)
            print("Chatbot:", resposta)

# Criar uma instância do Chatbot
chatbot = Chatbot()

# Iniciar a conversa
chatbot.iniciar_conversa()