"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""

class ProfessionalProfile:
    # Constructor:
    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree

    # Method:
    def info(self):
        print(f"Meu nome é {self.name}, a minha idade é {self.age} e sou {self.degree} em Física.")





if __name__ == "__main__":
    # Instanciar o objeto:
    professionalProfile = ProfessionalProfile("Eddy Giusepe", 42, "PhD")
    professionalProfile.info()
