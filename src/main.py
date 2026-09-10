import pandas as pd
from pathlib import Path

pasta_do_script = Path(__file__).resolve().parent
caminho_csv = pasta_do_script.parent / "data" / "flights.csv"

df = pd.read_csv(caminho_csv)
