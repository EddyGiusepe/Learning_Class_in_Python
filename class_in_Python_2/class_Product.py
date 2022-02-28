class Product:
    '''
    Esta classe representa um produto
    '''
    def __init__(self, name, price, size, company, wearType, gender):
        self.name = name
        self.price = price
        self.size = size
        self.company = company
        self.wearType = wearType
        self.gender = gender


    def __str__(self):
        return "O produto se chama {}, custo {}, é de tamanho {}, foi comprado na {}, é um(a) {} e é para gênero {}".format(self.name, self.price, self.size, self.company, self.wearType, self.gender)


    def __hash__(self):
        '''
        Retorna um código hash para o objeto de classe
        '''
        return hash((self.name, self.price, self.size, self.company, self.wearType, self.gender))

    def __eq__(self, other):
        '''
        Verifica se dois objetos são iguais ou não
        '''
        if not isinstance(other, Product):
            return False
        else:
            return (self.name, self.price, self.size, self.company, self.wearType, self.gender) == (other.name, other.price, other.size, other.company, other.wearType, other.gender)

if __name__ == "__main__":
    x = Product("Bonê", 50, "Medium", "Loja Katty", "Camisa", "Masculino")
    print(x)

