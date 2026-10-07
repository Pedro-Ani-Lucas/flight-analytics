import pandas as pd
from pathlib import Path

#Função para copiar o dataframe recebido sem precisar alterar o original.
def copiar_df(df):
    df_cpy = df.copy()

    return df_cpy

# 1 - Função para tratar a coluna airline sobre caracteres. Deixar padronizado.
def tratar_coluna_airline(df):
    df["airline"] = df["airline"].str.strip().str.upper()
    return df


# 2 - Resolver a coluna Delay Minutes sobre o valor NULL e sobre os valores anormais
def tratar_coluna_delay_minutes(df):
    df = df[(~df["delay_minutes"].isna()) & 
    (df["delay_minutes"] >= 0) & 
    (df["delay_minutes"] != 999)]
    return df

# 3 - Resolver a coluna Passengers sobre o valor NULL
def tratar_coluna_passengers(df):
    df = df[~df["passengers"].isna()]
    return df

# 4 - Resolver a tabela com duplicadas.
def tratar_linhas_duplicadas(df_limpo):
    df_limpo = df_limpo.drop_duplicates()
    return df_limpo


def transformar_df_voos(df):

    df_copiado = copiar_df(df)
    df_coluna_airline_tratado = tratar_coluna_airline(df_copiado)
    df_coluna_delay_minutes_tratado = tratar_coluna_delay_minutes(df_coluna_airline_tratado)
    df_coluna_passengers_tratado = tratar_coluna_passengers(df_coluna_delay_minutes_tratado)
    df_sem_duplicadas = tratar_linhas_duplicadas(df_coluna_passengers_tratado)
    df_transformado = df_sem_duplicadas

    return df_transformado