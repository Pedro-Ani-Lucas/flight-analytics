import sqlite3
from pathlib import Path

pasta_do_script = Path(__file__).resolve().parent

#Caminho para o flights.db
caminho_db_flights = pasta_do_script.parent / "database" / "flights.db"
caminho_db_flights.parent.mkdir(parents=True, exist_ok=True)

def quantidades_voos_por_companhia():
    conexao = sqlite3.connect(caminho_db_flights)
    cursor = conexao.cursor()

    resultado_quantidade = conexao.execute(
        """SELECT airline, COUNT(*)
        FROM flights
        GROUP BY airline;"""
    )

    print(resultado_quantidade.fetchall())