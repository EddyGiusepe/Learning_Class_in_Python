"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""

class Product:

    categoria = "Item de mercearia." # Atributo de classe
    
    def __init__(self, nome, marca, price):
        self.nome = nome # Atributo de instância
        self.marca = marca # Atributo de instância
        self.price = price # Atributo de instância


if __name__ == "__main__":
    # Criando os objetos:
    objeto1 = Product("Bike Ergonômica", "Goliat", 5325)
    objeto2 = Product("Laptop", "Dell", 25800)

    # Acessando Atributos:
    print(objeto1.categoria)

    # Acessando Atributos de instância:
    print(objeto2.nome)
