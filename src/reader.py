import csv

# USANDO DICTREADER PARA LER ARQUIVO CSV
def readerFlightsCSV():
    with open('data/csv/flights.csv', 'r', encoding='utf-8') as arquivo:

        readerFlights = csv.DictReader(arquivo)

        voos = list(readerFlights)

        return voos