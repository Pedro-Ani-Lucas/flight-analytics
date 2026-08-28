# 1 - Ler um arquivo CSV
import csv

def readerFlightsCSV():
    with open('flights.csv', 'r', encoding='utf-8') as arquivo:

        readerFlights = csv.reader(arquivo)

        print(f"Leitura concluída.")

        voos = list(readerFlights)

        return voos

# 2- Contar quantos voos existem.
def countFlightsExist():
    voos = readerFlightsCSV()

    for linha in voos[1:]:
        contador += 1
    return print(f"Há {contador} voos totais.")

# 3- Total de passageiros
def totalPassengers():
    total_passengers = 0
    voos = readerFlightsCSV()

    for linha in voos[1:]:
        total_passengers += int(linha[5])
    return print(f"Há no total de passageiros: {total_passengers}")

# 4- Descobrir atrasos(maior, menor e média)
maior = 0
menor = 0
media = 0


def calcDelay():
    voos = readerFlightsCSV()

    countFlightes = 0
    totalDelayFlightes = 0
    maior = 0
    menor = 0
    media = 0 

    for linha in voos[1:]:
        if int(linha[4]) > maior:
            maior = int(linha[4])
        elif int(linha[4]) >= menor and menor == 0:
            menor = int(linha[4])
        elif int(linha[4]) < menor:
            menor = int(linha[4])

        totalDelayFlightes += int(linha[4])
        countFlightes += 1

    media = totalDelayFlightes/countFlightes

    return maior, menor, media

# 5 - Descobrir a companhia com maior quantidade de voos.

def mostQuantityFlightesCompany():
    voos = readerFlightsCSV()

    for linha in voos[1:]:
        if linha[1] == "GOL":
            golFlightes += 1
        elif linha[1] == "AZUL":
            azulFlightes += 1
        elif linha[1] == "LATAM":
            latamFlightes += 1

    if(golFlightes > azulFlightes > latamFlightes):
        return print(f"A companhia com a maior quantidade de voo é a GOL com {golFlightes} voos.")
    elif(azulFlightes > golFlightes > latamFlightes):
        return print(f"A companhia com a maior quantidade de voo é a AZUL com {azulFlightes} voos.")
    else:
        return print(f"A companhia com a maior quantidade de voo é a LATAM com {latamFlightes} voos.")