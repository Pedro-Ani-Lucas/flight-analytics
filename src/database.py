import pandas as pd
import sqlite3
from pathlib import Path

def criar_conexao_sqlite():

    pasta_do_script = Path(__file__).resolve().parent

    caminho_db_flights = pasta_do_script.parent / "database" / "flights.db"
    caminho_db_flights.parent.mkdir(parents=True, exist_ok=True)

    conexao = sqlite3.connect(caminho_db_flights)

    return conexao

def criar_tabela_flights(conexao):
    cursor = conexao.cursor()

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

    cursor.execute(criar_tabela)
    conexao.commit()



df_limpo.to_sql("flights", conexao, if_exists="append", index=False)

