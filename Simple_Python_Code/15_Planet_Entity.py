#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
class CelestialBody:
    def __init__(self, name: str, distance_from_sun: float):
        self.details = {
            "name": name,
            "distance_from_sun": distance_from_sun
        }

    
class Planet(CelestialBody):
    def __init__(self, name, distance_from_sun, diameter):
        super().__init__(name, distance_from_sun)
        self.details["diameter"] = diameter




if __name__ == "__main__":
    solar_system = [Planet("Tierra", 149600000, 12756.2), Planet("Marte", 227940000, 6779)] # km
    resposta = solar_system[1].details["name"]
    print(f"O Planeta é: {resposta}")
