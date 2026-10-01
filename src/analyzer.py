import pandas as pd

#Função para saber o índice do maior percentual de atraso entre as companhias
def maiorindicepercentual_atrasoscompanhia(df):
    #1 - Criando um dataframe pegando a coluna de atrasos filtrando apenas os voos que realmente atrasaram.
    df["atrasados"] = df["delay_minutes"] > 0
    #2 - Assim, agrupando o dataframe com cada tipo de companhia e fazendo uma média com base no número de atrasos / voos totais e multiplicando por 100 por ser percentual.
    percentual_atraso = df.groupby("airline")["atrasados"].mean() * 100
    #3 - Descobrindo o maior percentual dentre as companhias.
    maior_percentual_atraso = percentual_atraso.max()
    #4 - Agora descobrindo o indíce do maior percentual de atraso
    companhia_maior_percentual_atraso = percentual_atraso.idxmax()
    #5 - Impressão do nome da companhia e o percentual de atraso dela
    return print(f"A companhia com maior percentual de atrasos é {companhia_maior_percentual_atraso}, com {maior_percentual_atraso}% em seus voos.")
