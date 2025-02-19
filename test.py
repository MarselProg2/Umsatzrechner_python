import csv

data = [
    {"Name": "Max", "Alter": 30, "Stadt": "Berlin"},
    {"Name": "Anna", "Alter": 22, "Stadt": "München"},
    {"Name": "Lukas", "Alter": 28, "Stadt": "Hamburg"}
]

# Öffne die CSV-Datei im Schreibmodus
with open('daten.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Alter", "Stadt"])
    
    # Schreibe die Header-Zeile (Spaltenüberschriften)
    writer.writeheader()
    
    # Schreibe jede Zeile mit den Daten
    for row in data:
        writer.writerow(row)
