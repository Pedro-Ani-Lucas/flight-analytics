import pandas as pd
from pathlib import Path
from clean_datas import limpeza_registros_voos

pasta_do_script = Path(__file__).resolve().parent
caminho_csv_flights = pasta_do_script.parent / "data" / "flights.csv"

caminho_csv_flights_raw = pasta_do_script.parent / "data" / "flights_raw.csv"

df_sujo = pd.read_csv(caminho_csv_flights_raw)

df_limpo = limpeza_registros_voos(df_sujo)

print(f"Quantidade de registros: {len(df_sujo)}")
print(f"Quantidade de registros: {len(df_limpo)}")
print(f"Quantidade de registros removidos: {len(df_sujo)-len(df_limpo)}")
