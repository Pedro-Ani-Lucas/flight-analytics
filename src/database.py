import pandas as pd
import sqlite3
from pathlib import Path

pasta_do_script = Path(__file__).resolve().parent

caminho_db_flights = pasta_do_script.parent / "database" / "flights.db"
caminho_db_flights.parent.mkdir(parents=True, exist_ok=True)

caminho_csv_flights_limpo = pasta_do_script.parent / "data" / "csv" / "flights_limpo.csv"

df_limpo = pd.read_csv(caminho_csv_flights_limpo)

#Conectar com o banco de dados
conexao = sqlite3.connect(caminho_db_flights)

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
visualizar_tabela_flights = """
SELECT * FROM flights;
"""

maior_indice_percentual_atrasos_por_companhia = """
SELECT airline, 100*AVG(CASE WHEN delay_minutes > 0 
THEN 1 ELSE 0 
END) AS atrasados
FROM flights
GROUP BY airline
ORDER BY atrasados DESC
LIMIT 1;
"""

resultado = conexao.execute(maior_indice_percentual_atrasos_por_companhia)
dados = resultado.fetchall()
print(dados)

#df_limpo.to_sql("flights", conexao, if_exists="append", index=False)

#conexao.commit()

conexao.close()
