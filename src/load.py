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

def inserir_dados_para_banco(df, conexao):
    
    df.to_sql("flights", conexao, if_exists="append", index=False)
    print(f"Inserção ao banco de dados concluída.")

def inserir_dataframelimpo_para_csv(df, caminho):
    
    caminho.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(caminho, sep=',', index=False, encoding='utf-8')

def load(df_limpo, caminho_csv):

    conexao = criar_conexao_sqlite()
    criar_tabela_flights(conexao)
    inserir_dados_para_banco(df_limpo, conexao)
    inserir_dataframelimpo_para_csv(df_limpo, caminho_csv)