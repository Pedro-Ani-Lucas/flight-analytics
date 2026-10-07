import pandas as pd
from pathlib import Path
from extract import extrair_voos
from transform import transformar_df_voos
from database import load

#CAMINHOS
pasta_do_script = Path(__file__).resolve().parent
caminho_csv_flights = pasta_do_script.parent / "data" / "csv" / "flights.csv"
caminho_csv_flights.parent.mkdir(parents=True, exist_ok=True)
caminho_csv_flights_raw = pasta_do_script.parent / "data" / "csv" / "flights_raw.csv"
caminho_csv_flights_raw.parent.mkdir(parents=True, exist_ok=True)

def main():
    df_raw = extrair_voos()
    df_limpo = transformar_df_voos(df_raw)
    load(df_limpo)

if __name__ == "__main__":
    main()
