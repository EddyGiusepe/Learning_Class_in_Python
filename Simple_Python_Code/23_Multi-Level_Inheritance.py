#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Multi-Level Inheritance (Herança Multi-Nível)
============================================
Herança Multi-Nível é um conceito em programação orientada a objetos
em que uma classe herda de outra classe, e uma terceira classe herda
da segunda classe, formando assim uma cadeia ou hierarquia de herança.
"""

class Vehicle:
    """Este será a classe Vovô"""
    def engine_type(self):
        print("Electric Engine")


class AutoMobile(Vehicle):
    """Este será a classe Pai"""
    wheel = 4
    def no_of_wheel(self):
        return self.wheel
    

class Car(AutoMobile):
    """Este será a classe Filho"""
    seat = 5
    def seat_count(self):
        return self.seat
    


if __name__ == '__main__':
    olaRide = Car()
    olaRide.engine_type()
    print(olaRide.no_of_wheel())
    print(olaRide.seat_count())
