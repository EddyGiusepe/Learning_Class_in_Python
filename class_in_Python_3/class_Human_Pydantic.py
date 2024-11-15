#!/usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
from typing import List, Optional
from pydantic import BaseModel, Field, field_validator

class Human(BaseModel):
    name: str = Field(..., min_length=2, description="Nome da pessoa") # name: str (obrigatório, indicado por ...)
    occupation: str = Field(..., description="Ocupação profissional") # occupation: str (obrigatório, indicado por ...)
    # Os campos que seguem são Atributos opcionais (têm valores padrão):
    age: Optional[int] = Field(None, ge=0, le=120, description="Idade da pessoa") # age: Optional[int] = None
    languages: List[str] = Field(default_factory=list, description="Idiomas falados") # languages: List[str] = [] (usando default_factory=list)
    skills: List[str] = Field(default_factory=list, description="Habilidades profissionais") # skills: List[str] = [] (usando default_factory=list)
    energy: int = Field(default=100, ge=0, le=100, description="Nível de energia") # energy: int = 100
    knowledge: int = Field(default=0, ge=0, description="Nível de conhecimento") # knowledge: int = 0

    @field_validator('occupation')
    def validate_occupation(cls, v):
        valid_occupations = ["Senior Data Scientist", "Soccer player", "Developer"]
        if v not in valid_occupations:
            raise ValueError(f"Ocupação deve ser uma das seguintes: {valid_occupations}")
        return v

    def work_that_does(self):
        if self.energy < 20:
            print(f"{self.name} está muito cansado(a) para trabalhar!")
            return
            
        self.energy = self.energy - 20 # self.energy -= 20
        
        if self.occupation == "Senior Data Scientist":
            print(f"{self.name} trabalha com Inteligência Artificial")
            self.knowledge += 5
        elif self.occupation == "Soccer player":
            print(f"{self.name} joga futebol profissionalmente")
            self.energy -= 10
        else:
            print(f"{self.name} trabalha em outra área")

    def rest(self, hours: int):
        energy_recovered = hours * 10
        self.energy = min(100, self.energy + energy_recovered)
        print(f"{self.name} descansou e recuperou energia. Energia atual: {self.energy}")

    def learn_language(self, language: str):
        if language not in self.languages:
            self.languages.append(language)
            self.knowledge += 2
            print(f"{self.name} aprendeu {language}!")
        else:
            print(f"{self.name} já sabe {language}")

    class Config:
        validate_assignment = True  # Valida também alterações após a criação



if __name__ == "__main__":
    try:
        # Criando uma instância válida
        ed = Human(
            name="Eddy",
            occupation="Senior Data Scientist",
            age=30,
            languages=["Português", "Espanhol"],
            skills=["Python", "Machine Learning", "Deep Learning"]
        )
        
        print(ed.model_dump_json(indent=2))  # Mostra os dados em formato JSON
        
        # Testando os métodos
        ed.work_that_does()
        ed.learn_language("Inglês")
        
        # # Tentativa inválida (vai gerar erro)
        # invalid_human = Human(
        #     name="X",  # Nome muito curto
        #     occupation="Chef",  # Ocupação não permitida
        #     age=150  # Idade maior que o permitido
        # )
        
    except ValueError as e:
        print(f"Erro de validação: {e}")