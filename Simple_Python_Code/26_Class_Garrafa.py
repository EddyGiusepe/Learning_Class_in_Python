#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
class GarrafaGatorade:
    def __init__(self, price: float = 5.20, height: float = 20, volume: float = None):
        """
        Inicializa uma nova instância da classe GarrafaGatorade.

        :param price: Preço da garrafa em reais.
        :param height: Altura da garrafa em centímetros.
        :param volume: Volume da garrafa em mililitros.
        """
        if price < 0:
            raise ValueError("O preço não pode ser negativo.")
        if height <= 0:
            raise ValueError("A altura deve ser maior que zero.")
        if volume is not None and volume <= 0:
            raise ValueError("O volume deve ser maior que zero.")
        
        self._price = price
        self._height = height
        self._volume = volume

    @property
    def price(self) -> float:
        return self._price

    @property
    def height(self) -> float:
        return self._height

    @property
    def volume(self) -> float:
        return self._volume

    def custo_da_garrafa(self) -> str:
        """
        Retorna uma string com o custo da garrafa.
        """
        return f"O preço da bebida Gatorade é: R$ {self.price:.2f}"

    def altura_e_volume(self) -> str:
        """
        Retorna uma string com a altura e o volume da garrafa.
        """
        volume_info = f"e tem um volume de {self.volume} ml." if self.volume else "e o volume não foi especificado."
        return f"A altura da garrafa é de {self.height} cm {volume_info}."

if __name__ == '__main__':
    try:
        garrafa = GarrafaGatorade(price=5.50, height=20, volume=500)
        print(garrafa.custo_da_garrafa())
        print("")
        print(garrafa.altura_e_volume())
    except ValueError as e:
        print(f"Erro: {e}")