#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""

import time
import sys
import keyboard

try:
    from tqdm import tqdm
except ImportError:
    sys.exit("Erro: Módulo 'tqdm' não encontrado. Por favor instale usando: 'pip install tqdm'.")


def loading_bar(total_iterations=100, bar_description="Loading . . .", sleep_duration=0.01, abort_key=None):
    """
    Exibe uma barra de progresso durante a execução das iterações:

    Args:

    total_iterations (int)
    bar_description (str)
    sleep_duration (float): A duração do sleep entre iterações (Em segundos).
    abort_key (str ou None): Default is None.
    """
    for i in tqdm(range(total_iterations), desc=bar_description, ascii=False, ncols=75, unit=""):
        if abort_key and keyboard.is_pressed(abort_key):
            print("\nProgresso abordado pelo Usuário")
            break
        time.sleep(sleep_duration)




if __name__ == "__main__":
    abort_key = input("Insira uma key para cancelar o progresso (ou pressione Enter para desativar a interrupção): ")
    loading_bar(total_iterations=100, bar_description="Processando os Dados", sleep_duration=0.02, abort_key=abort_key)
