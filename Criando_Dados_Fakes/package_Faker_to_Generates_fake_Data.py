"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Faker
=====
Faker é um pacote Python que gera dados falsos para você. Se você precisa
inicializar seu banco de dados, criar documentos XML bonitos, preencher 
sua persistência para testá-lo ou tornar anônimos dados obtidos de um serviço
de produção, o Faker é para você.

Link de estudo --> https://pypi.org/project/Faker/

NOTA: Ver a documentação porque não para todos os lugares 
      existem os mesmos métodos.

"""

from faker import Faker
from decimal import Decimal

def generate_fake_Data(locale='en_US', quantity=5):


    try:
        fake = Faker(locale)
    except ValueError:
        print(f"Localidade '{locale}' não é válida. Usando o padrão 'en_US'")
        fake = Faker()

    data = {
        "names": [fake.name() for _ in range(quantity)],
        "addresses": [fake.address() for _ in range(quantity)],
        #"texts": [fake.text() for _ in range(quantity)],
        "emails": [fake.email() for _ in range(quantity)],
        "countries": [fake.country() for _ in range(quantity)],
        "phone_numbers": [fake.phone_number() for _ in range(quantity)],
        "urls": [fake.url() for _ in range(quantity)],
        "dates": [fake.date() for _ in range(quantity)],
        "coordinates": [(fake.latitude(), fake.longitude()) for _ in range(quantity)]
    }
    return data

if __name__ == "__main__":
    # Exemplo de uso do Faker e exibição dos dados gerados:
    fake_data = generate_fake_Data(locale='pt_BR', quantity=3) # 'es_ES' 'es_MX'   'pt_BR'
    # Ver Localized Providers --> https://faker.readthedocs.io/en/stable/locales.html

    for key, values in fake_data.items():
        print(f"{key}: ")
        for value in values:
            print(value)
        print("")    