import sqlite3
from pathlib import Path

pasta_do_script = Path(__file__).resolve().parent

#Caminho para o flights.db
caminho_db_flights = pasta_do_script.parent / "database" / "flights.db"
caminho_db_flights.parent.mkdir(parents=True, exist_ok=True)

#CONSULTAS SQL
def quantidades_voos_por_companhia():
    conexao = sqlite3.connect(caminho_db_flights)

    resultado_quantidade = conexao.execute(
        """SELECT airline, COUNT(*)
        FROM flights
        GROUP BY airline;"""
    )

    print(resultado_quantidade.fetchall())

    conexao.close()

def media_de_atrasos_geral():
    conexao = sqlite3.connect(caminho_db_flights)

    resultado_media = conexao.execute(
        """SELECT AVG(delay_minutes)
        FROM flights;"""
    )

    print(resultado_media.fetchall())

    conexao.close()

def media_atrasos_por_companhia():
    conexao = sqlite3.connect(caminho_db_flights)

    resultado_media_por_companhia = conexao.execute(
        """SELECT airline, AVG(delay_minutes)
        FROM flights
        GROUP BY airline
        ORDER BY AVG(delay_minutes) DESC;"""
    )

    print(resultado_media_por_companhia.fetchall())

    conexao.close()

#Qual aeroporto possui a pior média de atraso?

def pior_media_de_atraso_por_aeroporto_origem():
    conexao = sqlite3.connect(caminho_db_flights)

    pior_atraso_aeroportoorigem = conexao.execute(
        """
        SELECT origin, AVG(delay_minutes)
        FROM flights
        GROUP BY origin
        ORDER BY AVG(delay_minutes) DESC
        LIMIT 1;
        """
    )

    print(pior_atraso_aeroportoorigem.fetchall())

    conexao.close()

def pior_media_de_atraso_por_aeroporto_destino():
    conexao = sqlite3.connect(caminho_db_flights)

    pior_atraso_aeroportodestino = conexao.execute(
        """
        SELECT destination, AVG(delay_minutes)
        FROM flights
        GROUP BY destination
        ORDER BY AVG(delay_minutes) DESC
        LIMIT 1;
        """
    )

    print(pior_atraso_aeroportodestino.fetchall())

    conexao.close()

def visualizar_tabela_inteira():
    conexao = sqlite3.connect(caminho_db_flights)

    visualizar_tabela_flights = conexao.execute( 
    """
    SELECT * FROM flights;
    """
    )

    print(visualizar_tabela_flights.fetchall())
    
    conexao.close()

def visualizar_maior_indice_percentual_atrasos_por_companhia():

    conexao = sqlite3.connect(caminho_db_flights)

    maior_indice_percentual_atrasos_por_companhia = conexao.execute(
    """
    SELECT airline, 100*AVG(CASE WHEN delay_minutes > 0 
    THEN 1 ELSE 0 
    END) AS atrasados
    FROM flights
    GROUP BY airline
    ORDER BY atrasados DESC
    LIMIT 1;
    """
    )
    print(maior_indice_percentual_atrasos_por_companhia.fetchall())
    
    conexao.close()