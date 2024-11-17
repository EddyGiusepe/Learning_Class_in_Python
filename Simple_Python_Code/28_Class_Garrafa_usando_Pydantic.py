#!/usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
from pydantic import BaseModel, Field, field_validator
from typing import Optional
import logging
from colorama import Fore, Style, init
# Inicializando o colorama:
init(autoreset=True)


class GarrafaGatorade(BaseModel):
    price: float = Field(default=5.20, gt=0, description="Preço da garrafa em reais.")
    height: float = Field(default=20.0, gt=0, description="Altura da garrafa em centímetros.")
    volume: Optional[float] = Field(default=None, gt=0, description="Volume da garrafa em mililitros.")

    @field_validator('volume')
    @classmethod
    def check_volume(cls, v: Optional[float]) -> Optional[float]:
        if v is not None and v <= 0:
            raise ValueError("O volume, se fornecido, deve ser positivo.")
        return v

    @property # Para usar o método como se fosse um ATRIBUTO
    def custo_da_garrafa(self) -> str:
        return f"O preço da bebida Gatorade é: R$ {self.price:.2f}"

    @property # Para usar o método como se fosse um ATRIBUTO
    def altura_e_volume(self) -> str:
        volume_str = f"{self.volume:.1f}" if self.volume is not None else "volume não fornecido"
        return f"A altura da garrafa é de {self.height:.1f} cm e tem um volume de {volume_str} ml."





if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info(f"{Fore.RED}Iniciando a Instância da classe{Style.RESET_ALL}")
    try:
        garrafa = GarrafaGatorade(price=5.50, height=20, volume=500)
        print(garrafa.custo_da_garrafa)
        print(garrafa.altura_e_volume)
        
        # Exemplo de serialização:
        print(f"{Fore.BLUE}A serialização --->{Style.RESET_ALL} {garrafa.model_dump_json()}")
        
        # Exemplo de criação a partir de um dicionário:
        dados = {"price": 6.0, "height": 22.0, "volume": 600}
        garrafa2 = GarrafaGatorade(**dados)
        print(garrafa2)
        print("")
        logging.info(f"{Fore.GREEN}Finalizando a execução do script{Style.RESET_ALL}")    
    except ValueError as e:
        logging.error(f"Erro ao criar garrafa: {e}")








