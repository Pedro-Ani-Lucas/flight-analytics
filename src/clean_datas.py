import pandas as pd
from pathlib import Path

pasta_do_script = Path(__file__).resolve().parent
caminho_csv = pasta_do_script.parent / "data" / "flights_raw.csv"

df = pd.read_csv(caminho_csv)

# 1 - Resolver a coluna Airline

df["airline"] = df["airline"].str.strip().str.upper()

# 2 - Resolver a coluna Delay Minutes sobre o valor NULL e sobre os valores anormais

df_limpo = df[(~df["delay_minutes"].isna()) & 
            (df["delay_minutes"] >= 0) & 
            (df["delay_minutes"] != 999)]

# 3 - Resolver a coluna Passengers sobre o valor NULL

df_limpo = df_limpo[~df_limpo["passengers"].isna()]

