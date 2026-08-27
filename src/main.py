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
    print(f"Há {contador} voos.")

# 3- Total de passageiros
def totalPassengers():
    total_passengers = 0
    voos = readerFlightsCSV()

    for linha in voos:
        total_passengers += int[linha[5]]
    print(f"Há no total de passageiros: {total_passengers}")

# 4- Descobrir atrasos

