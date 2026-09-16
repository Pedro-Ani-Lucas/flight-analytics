import pandas as pd
from pathlib import Path

pasta_do_script = Path(__file__).resolve().parent
caminho_csv_flights = pasta_do_script.parent / "data" / "flights.csv"

caminho_csv_flights_raw = pasta_do_script.parent / "data" / "flights_raw.csv"

