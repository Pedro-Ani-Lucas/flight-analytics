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

    conexao.close()

def media_de_atrasos_geral():
    conexao = sqlite3.connect(caminho_db_flights)
    cursor = conexao.cursor()

    resultado_media = conexao.execute(
        """SELECT AVG(delay_minutes)
        FROM flights;"""
    )

    print(resultado_media.fetchall())

    conexao.close()

def media_atrasos_por_companhia():
    conexao = sqlite3.connect(caminho_db_flights)
    cursor = conexao.cursor()

    resultado_media_por_companhia = conexao.execute(
        """SELECT airline, AVG(delay_minutes)
        FROM flights
        GROUP BY airline
        ORDER BY AVG(delay_minutes) DESC;"""
    )

    print(resultado_media_por_companhia.fetchall())

    conexao.close()