#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
def stem_words(sentence):
    # Divide a sequência em palavras individuais
    words = sentence.split()
    stemmed_words = []

    # Processa cada palavra na sequência
    for word in words:
        # Remove os sufixos "ed", "ly" ou "ing", se presentes
        if word.endswith("ed"):
            word = word[:-2]
        elif word.endswith("ly"):
            word = word[:-2]
        elif word.endswith("ing"):
            word = word[:-3]
        
        # Mantém apenas as primeiras 8 letras, se a palavra resultante for mais longa
        if len(word) > 8:
            word = word[:8]
        
        # Adiciona a palavra radical à lista de palavras resultantes
        stemmed_words.append(word)
    
    # Retorna a sequência de palavras radicalizadas como uma string
    return ' '.join(stemmed_words)

# Exemplo de uso da função
sentence = "worked lovingly singing playing"
stemmed_sentence = stem_words(sentence)
print(stemmed_sentence)





