#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""

class Sport:
    def __init__(self, name: str):
        self.name = name


class Football(Sport):
    def __init__(self, teams: list[str]):
        super().__init__("Football")
        self.teams = teams

    def match(self):
        return f"{self.name} match: {self.teams[0]} vs {self.teams[1]}"
    


if __name__ == "__main__":
    objeto = Football(["Team A", "Team B"])
    response = objeto.match()
    print(response)
