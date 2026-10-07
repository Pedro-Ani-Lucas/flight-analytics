from pathlib import Path
from extract import extrair_voos
from transform import transformar_df_voos
from load import load

#CAMINHOS
pasta_do_script = Path(__file__).resolve().parent
caminho_csv_processed = pasta_do_script.parent / "data" / "csv" / "processed" / "flights_processed.csv"

def main():
    df_raw = extrair_voos()
    df_limpo = transformar_df_voos(df_raw)
    load(df_limpo, caminho_csv_processed)

if __name__ == "__main__":
    main()
