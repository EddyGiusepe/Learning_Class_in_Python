#! /usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Execução do script
==================

$ uvicorn main:app --reload
"""
from typing import Dict, Any
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from generate import generate
import uvicorn
import os
from dotenv import load_dotenv, find_dotenv

# Constantes
API_TITLE = "🤗 Aplicativo de LLM com FastAPI e OpenAI 🤗"
API_VERSION = "1.0.0"
API_DESCRIPTION = "Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro"
HOST = "0.0.0.0"
PORT = 80
MODEL_NAME = "gpt-4o-2024-11-20" # "gpt-4-0125-preview"  
TEMPERATURE = 0.0

class LLMConfig:
    """Configuração do modelo de linguagem."""
    def __init__(self) -> None:
        """Inicializa as configurações do LLM."""
        _ = load_dotenv(find_dotenv())
        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            temperature=TEMPERATURE
        )

class Body(BaseModel):
    """Modelo Pydantic para o corpo da requisição."""
    text: str

    class Config:
        """Configuração do modelo Pydantic."""
        json_schema_extra = {
            "example": {
                "text": "Qual é a capital do Brasil?"
            }
        }

class LLMApp:
    """Classe principal do aplicativo FastAPI."""
    
    def __init__(self) -> None:
        """Inicializa o aplicativo FastAPI e suas configurações."""
        self.app = FastAPI(
            title=API_TITLE,
            version=API_VERSION,
            description=API_DESCRIPTION
        )
        self.llm_config = LLMConfig()
        self._setup_routes()

    def _setup_routes(self) -> None:
        """Configura as rotas do aplicativo."""
        self.app.get("/")(self.welcome)
        self.app.post("/response")(self.generate_response)

    @staticmethod
    async def welcome() -> Dict[str, str]:
        """Rota de boas-vindas.
        
        Returns:
            Dict[str, str]: Mensagem de boas-vindas
        """
        return {"message": "Bem-vindo ao LLMApp!"}

    async def generate_response(self, body: Body) -> Dict[str, Any]:
        """Gera uma resposta usando o modelo de linguagem.
        
        Args:
            body (Body): Corpo da requisição contendo o texto
            
        Returns:
            Dict[str, Any]: Resposta gerada pelo modelo
        """
        question = body.text
        result = generate(question, self.llm_config.llm, PromptTemplate)
        return {"response": result}

def create_app() -> FastAPI:
    """Cria e retorna a instância do aplicativo.
    
    Returns:
        FastAPI: Instância configurada do aplicativo
    """
    llm_app = LLMApp()
    return llm_app.app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
