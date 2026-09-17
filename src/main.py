import pandas as pd
from pathlib import Path
from clean_datas import limpeza_registros_voos

#CAMINHOS
pasta_do_script = Path(__file__).resolve().parent
caminho_csv_flights = pasta_do_script.parent / "data" / "csv" / "flights.csv"
caminho_csv_flights.parent.mkdir(parents=True, exist_ok=True)
caminho_csv_flights_raw = pasta_do_script.parent / "data" / "csv" / "flights_raw.csv"
caminho_csv_flights_raw.parent.mkdir(parents=True, exist_ok=True)

df_sujo = pd.read_csv(caminho_csv_flights_raw)

df_limpo = limpeza_registros_voos(df_sujo)

#Saí de SRC e entra na pasta DATA por conta do .parent e coloca um nome pro arquivo novo
caminho_saida = pasta_do_script.parent / "data" / "csv" / "flights_limpo.csv"
#Confere se realmente existe a pasta Data para então entrar nela.
caminho_saida.parent.mkdir(parents=True, exist_ok=True)
#Agora lança o dataframe, convertido em csv, para a pasta correta.
df_limpo.to_csv(caminho_saida, index=False)
