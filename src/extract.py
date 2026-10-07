import csv
import pandas as pd
from pathlib import Path

def extrair_csv_voos():
    pasta_do_script = Path(__file__).resolve().parent
    caminho_csv = pasta_do_script / "data" / "csv" / "flights_raw.csv"
    return leitor_csv(caminho_csv)

def leitor_csv(caminho):
    
    df = pd.read_csv(caminho)

    return df




def extrair_voos():
    df = extrair_csv_voos()
    return df

