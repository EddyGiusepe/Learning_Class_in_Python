#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""

perguntas_respostas = {
    "olá": "Olá! Como você está?",
    "tchau": "Tchau! Até mais!",
    "como você está": "Estou bem, obrigado!",
    "quem é você": "Sou um Chatbot simples criado em Python!",
    "ajuda": "Posso ajudar com perguntas básicas. Tente me perguntar algo!"
}


class MeuChatBot:
    def chatbot(self, pergunta):
        pergunta = pergunta.lower()  # converter para minúscula
        if pergunta in perguntas_respostas:
            return perguntas_respostas[pergunta]
        else:
            return "Desculpe, não entendi. Tente novamente!"


if __name__=="__main__":
    print("Bem-vindo ao Chatbot!")
    chat = MeuChatBot()
    while True:
        pergunta = input("Você: ")
        resposta = chat.chatbot(pergunta)
        print("Chatbot:", resposta)