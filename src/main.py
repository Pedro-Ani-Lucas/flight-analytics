# 1 - Ler um arquivo CSV
import csv

def readerFlightsCSV():
    with open('data/flights.csv', 'r', encoding='utf-8') as arquivo:

        readerFlights = csv.DictReader(arquivo)

        voos = list(readerFlights)

        return voos

# 2- Contar quantos voos existem.
def countFlightsExist():
    voos = readerFlightsCSV()
    contador = 0
    for linha in voos:
        contador += 1
    return print(f"Há {contador} voos totais.")

# 3- Total de passageiros
def totalPassengers():
    total_passengers = 0
    voos = readerFlightsCSV()

    for linha in voos:
        total_passengers += int(linha["passengers"])
    return print(f"Há no total de passageiros: {total_passengers}")

# 4- Descobrir atrasos(maior, menor e média)
maior = 0
menor = 0
media = 0


def calcDelay():
    voos = readerFlightsCSV()

    countFlightes = 0
    totalDelayFlightes = 0
    maior = int(voos[0]["delay_minutes"])
    menor = int(voos[0]["delay_minutes"])
    media = 0 

    for linha in voos:
        if int(linha["delay_minutes"]) > maior:
            maior = int(linha["delay_minutes"])
        elif int(linha["delay_minutes"]) < menor:
            menor = int(linha["delay_minutes"])

        totalDelayFlightes += int(linha["delay_minutes"])
        countFlightes += 1

    media = totalDelayFlightes/countFlightes

    return print(f"Maior minutos de delay: {maior} | Menor minutos de delay: {menor} | Média de Delay por voo: {media:.2f}")

# 5 - Descobrir a companhia com maior quantidade de voos.

def mostQuantityFlightesCompany():
    voos = readerFlightsCSV()
    golFlightes = 0
    azulFlightes = 0
    latamFlightes = 0

    for linha in voos:
        if linha["airline"] == "GOL":
            golFlightes += 1
        elif linha["airline"] == "AZUL":
            azulFlightes += 1
        elif linha["airline"] == "LATAM":
            latamFlightes += 1

    if(golFlightes > azulFlightes > latamFlightes):
        return print(f"A companhia com a maior quantidade de voo é a GOL com {golFlightes} voos.")
    elif(azulFlightes > golFlightes > latamFlightes):
        return print(f"A companhia com a maior quantidade de voo é a AZUL com {azulFlightes} voos.")
    else:
        return print(f"A companhia com a maior quantidade de voo é a LATAM com {latamFlightes} voos.")

# TESTE PRÁTICO

readerFlightsCSV()
countFlightsExist()
totalPassengers()
calcDelay()
mostQuantityFlightesCompany()