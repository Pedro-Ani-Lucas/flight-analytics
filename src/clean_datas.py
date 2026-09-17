import pandas as pd
from pathlib import Path

def limpeza_registros_voos(df):
        df = df.copy()

        # 1 - Resolver a coluna Airline
        df["airline"] = df["airline"].str.strip().str.upper()

        # 2 - Resolver a coluna Delay Minutes sobre o valor NULL e sobre os valores anormais
        df = df[(~df["delay_minutes"].isna()) & 
        (df["delay_minutes"] >= 0) & 
        (df["delay_minutes"] != 999)]

        # 3 - Resolver a coluna Passengers sobre o valor NULL
        df_limpo = df[~df["passengers"].isna()]

        return df_limpo 

# Condicional para conferir se está chamando o arquivo diretamente ou importando.
if __name__ == "__main__":
        pasta_do_script = Path(__file__).resolve().parent
        caminho_csv = pasta_do_script.parent / "data" / "csv" / "flights_raw.csv"
        caminho_csv.parent.mkdir(parents=True, exist_ok=True)
        df = pd.read_csv(caminho_csv)
        print(limpeza_registros_voos(df))