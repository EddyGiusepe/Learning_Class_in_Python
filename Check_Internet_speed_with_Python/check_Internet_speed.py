#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Com este script você pode verificar a rapidez da sua Internet.

Instale (https://pypi.org/project/speedtest-cli/):

$ pip install speedtest-cli
"""

import speedtest

speed_test = speedtest.Speedtest()

def bytes_to_mb(bytes):
    KB = 1024 # Um kilobyte (KB) é o equivalente a 1024 Byte. ( 1B = 8 Bit )
    MB = KB * 1024 # Um MB é equivalente a 1024 KB 
    return int(bytes / MB)

download_speed = bytes_to_mb(speed_test.download())

print("A sua velocidade de Download é: ", download_speed, "MB")
