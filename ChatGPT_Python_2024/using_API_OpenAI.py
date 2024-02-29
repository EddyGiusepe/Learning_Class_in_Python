#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Usando a API da OpenAI para criar um ChatBot
============================================
Aqui mostramos um pequeno exemplo de como usar
a API da OpenAI.
"""
import openai
import config
from openai import OpenAI
import typer
from rich import print
from rich.table import Table


def main():

    openai.api_key = config.api_key
    print("")
    print("[bold green]Usando a API da OpenAI[/bold green]")
    
    table = Table("Comando", "Descrição")
    table.add_row("exit", "Para sair da aplicação")
    table.add_row("new", "Criar um novo bate-papo" )
    
    print(table)
    
    # Contexto do assistente    
    context = {"role": "system",
                "content": "Você é um assistente muito útil"}
    
    messages = [context]

    while True:
        
        content = __prompt()

        if content == "new" :
            print("Novo bate-papo criado")
            messages = [context]
            content = __prompt()
        
        messages.append({"role": "user", "content": content})

        response = openai.chat.completions.create(model="gpt-3.5-turbo",
                                                  messages=messages,
                                                  temperature=0.0,
                                                  #max_tokens=50
                                                 )

        response_content = response.choices[0].message.content
        
        messages.append({"role": "assistant", "content": response_content}) 
        
        print(f"[bold green]> [/bold green][green]{response_content}[/green]")
        
def __prompt() -> str:
    promt = typer.prompt("\nSobre que você gostaria de falar? ")

    if promt == "exit":
        exit = typer.confirm("Tem certeza que deseja sair?")
        if exit:
            print("Até mais!")
            raise typer.Abort()
        
        return __prompt()
    
    return promt
    
           
if __name__ == "__main__":
    typer.run(main)