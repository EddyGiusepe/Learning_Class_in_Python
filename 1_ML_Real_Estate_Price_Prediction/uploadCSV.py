#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Carregar arquivo CSV
====================
Aqui criamos uma classe bem simples para apenas carregar
um arquivo CSV e logo transformar para um DataFrame usando
a biblioteca do "pandas".
"""

import pandas as pd

class UploadCSV:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv_to_dataframe(self):
        """
        Carrega o arquivo CSV e retorna um DataFrame do Pandas.
        """
        try:
            dataframe = pd.read_csv(self.file_path)
            return dataframe
        except FileNotFoundError:
            print(f"Arquivo CSV '{self.file_path}' não encontrado")
            return None
        except Exception as e:
            print(f"Erro ao ler o arquivo CSV: {e}")




# Exemplo de uso:
if __name__ == "__main__":
    file_path = "./Real_Estate.csv"
    loader = UploadCSV(file_path=file_path)
    df = loader.read_csv_to_dataframe()

    if df is not None:
        print("DataFrame carregado com sucesso:")
        print(df.head())
    else:
        print("Erro ao carregar o arquivo CSV.")
