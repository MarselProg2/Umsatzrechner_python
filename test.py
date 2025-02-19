import pandas as pd

# Angenommene 'berechnungen' Liste als Beispiel:
berechnungen = [
    {'Rechnung_Nr': '001', 'Kunde': 'Max Mustermann', 'Betrag': 100.5, 'Datum': '2025-02-19'},
    {'Rechnung_Nr': '002', 'Kunde': 'Erika Musterfrau', 'Betrag': 200.75, 'Datum': '2025-02-20'},
    {'Rechnung_Nr': '003', 'Kunde': 'Hans Beispiel', 'Betrag': 50.0, 'Datum': '2025-02-21'}
]

# Schreiben in eine CSV-Datei
import csv
with open("Rechnungen.csv", mode="w", newline='') as csvfile:
    fieldnames = berechnungen[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in berechnungen:
        writer.writerow(row)

# Einlesen der CSV-Datei mit Pandas
df = pd.read_csv("Rechnungen.csv")

# Darstellung als Tabelle
print(df)
