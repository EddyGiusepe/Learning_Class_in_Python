#!/usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Ferramentas Industriais Dionisia
================================
Aqui vou construir uma classe para representar uma loja de ferramentas industriais.
"""
import json

class IndustrialToolsStore:
    def __init__(self, name: str, nationality: str, products: list[str], location: str=None):
        self.name = name
        self.nationality = nationality
        self.location = location
        self.products = products

    def type_of_company(self):
        if self.nationality == "Brasileiro":
            print(f"A empresa {self.name} é brasileira.")
        elif self.nationality == "Asiática":
            print(f"A empresa {self.name} é asiática.")
        elif self.nationality == "Europeia":
            print(f"A empresa {self.name} é europeia.")
        elif self.nationality == "Peruana":
            print(f"A empresa {self.name} é peruana.")
        else:
            print(f"A empresa {self.name} é de outro país")

    def add_product(self, product: str):
        self.products.append(product)

    def remove_product(self, product: str):
        if product in self.products:
            self.products.remove(product)
            return True
        return False
    
    def list_products(self):
        print(f"Produtos disponíveis na loja de {self.name}:")
        for product in self.products:
            print(f"- {product}")

    def update_location(self, new_location: str):
        self.location = new_location

    def get_store_info(self)-> dict:
        # Retorna um dicionário com as informações da loja:
        info = {
                "nome": self.name,
                "nacionalidade": self.nationality,
                "localização": self.location,
                "produtos": self.products
               }
        return info 
    
    @property # Decorador que permite que você defina um método que pode ser acessado como se fosse um atributo da classe
    def product_count(self)-> int:
        """Retorna a quantidade de produtos diferentes na loja"""
        return len(self.products)


if __name__ == "__main__":
    store = IndustrialToolsStore("Dionisia", "Peruana", ["Máquina de soldagem", "Soldadura", "Equipamentos EPIs"])
    store.type_of_company()
    
    print("")
    print("Adicionamos um Produto: ")
    store.add_product("Discos abrasivos")
    store.add_product("Martelos")
    store.add_product("Soldadura")

    print("")
    store.list_products()

    print(f"Total de produtos: {store.product_count}")
    store.update_location("Lima - Perú")

    print(json.dumps(store.get_store_info(), indent=4, ensure_ascii=False))
