#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""

class Telephone:
    def __init__(self):
        self.__number = None

    def dial(self, number):
        self.__number = number
        return f"Discando {self.__number}"
    

if __name__ == "__main__":
    phone = Telephone()
    response = phone.dial("887655123")
    print(response)
    