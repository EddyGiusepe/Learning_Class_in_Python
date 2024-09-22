#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
from dataclasses import dataclass
from typing import Optional
import logging
from colorama import Fore, Style, init
# Inicializando o colorama
init(autoreset=True)

@dataclass
class GarrafaGatorade:        
    price: float = 5.20
    height: float = 20.0
    volume: Optional[float] = None

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError("O preço deve ser positivo.")
        if self.height <= 0:
            raise ValueError("A altura deve ser positiva.")
        if self.volume is not None and self.volume <= 0:
            raise ValueError("O volume, se fornecido, deve ser positivo.")

    @property
    def custo_da_garrafa(self) -> str:
        return f"O preço da bebida Gatorade é: R$ {self.price:.2f}"

    @property
    def altura_e_volume(self) -> str:
        return f"A altura da garrafa é de {self.height:.1f} cm e tem um volume de {self.volume:.1f} ml."





if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info(f"{Fore.RED}Iniciando a Instância da classe{Style.RESET_ALL}")
    try:
        garrafa = GarrafaGatorade(price=5.50, height=20, volume=500)
        print(garrafa.custo_da_garrafa) # Quando usamos '@property', custo_da_garrafa se comporta como um atributo. Ou seja, você não usa parênteses 
        print(garrafa.altura_e_volume)
    except ValueError as e:
        logging.error(f"Erro ao criar garrafa: {e}")
