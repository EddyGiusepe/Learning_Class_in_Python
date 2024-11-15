#!/usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Class Human
===========
Aqui vou praticar construindo uma classe Human.
Lembrando os conceitos e usando outras técnicas.
"""
class Human:
    def __init__(self, name: str, occupation: str) -> None:
        self.name = name
        self.occupation = occupation

    def work_that_does(self):
        if self.occupation == "Senior Data Scientist":
            print(f"{self.name}, works with Artificial Intelligence")
        elif self.occupation == "Soccer player":
            print(f"{self.name}, plays soccer")
        else:
            print(f"{self.name}, works in other field")

    def languages_spoken(self):
        if self.occupation == "Senior Data Scientist":
            print(f"{self.name}, speaks Spanish and Portuguese")
        elif self.occupation == "Soccer player":
            print(f"{self.name}, doesn't speak English")



if __name__ == "__main__":
    ed = Human("Eddy", "Senior Data Scientist")
    print(ed.name)
    print("")
    ed.work_that_does()
    print("")
    ed.languages_spoken()
