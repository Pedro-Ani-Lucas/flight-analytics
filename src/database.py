import pandas as pd
import sqlite3
from pathlib import Path

pasta_do_script = Path(__file__).resolve().parent
caminho_db_flights = pasta_do_script.parent / "data" / "flights.db"
caminho_csv_flights_limpo = pasta_do_script.parent / "data" / "flights_limpo.csv"

df_limpo = pd.read_csv(caminho_csv_flights_limpo)

#Conectar com o banco de dados
connect = sqlite3.connect(caminho_db_flights)

cursor = connect.cursor()

criar_tabela = """
CREATE TABLE IF NOT EXISTS flights (
    flight_id INTEGER PRIMARY KEY,
    airline TEXT NOT NULL,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    delay_minutes INTEGER NOT NULL,
    passengers INTEGER NOT NULL,
    date TEXT NOT NULL
)
"""

inserir_dados = """

"""

connect.execute(criar_tabela)
connect.commit()

connect.close()
