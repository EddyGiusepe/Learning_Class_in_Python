#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Docker com IA ​​generativa
========================
O pessoal do Docker criaram uma ferramenta CLI --> "docker init".

O que é "docker init"?
--------------------
docker init é um utilitário de linha de comando que ajuda na inicialização de recursos Docker
dentro de um projeto. Ele cria Dockerfiles, arquivos Compose e arquivos .dockerignore com
base nos requisitos do projeto. Isso simplifica o processo de configuração do Docker para o
seu projeto, economizando tempo e reduzindo a complexidade.

A versão mais recente de "docker init" suporta Go, Python, Node.js, Rust, ASP.NET, PHP e Java.
Está disponível com Docker Desktop.


Link de estudo:

* https://medium.com/kpmg-uk-engineering/you-should-stop-writing-dockerfiles-today-do-this-instead-3cd8a44cb8b0


NOTA:

* Para usar "$ docker init" na linha de comando, você deve instalar o Docker para Desktop, etc.

* Leia a link de pesquisa 🤗!!!

* So executar -->  $ docker init
  e siga as instruções.
"""



from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_docker():
    return '<h1> Olá, Eddy Giusepe </h1'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    