import csv

with open("names.csv", mode="w") as csvfile:
    fieldnames = ["first_name", "last_name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"first_name": "John", "last_name": "Smith"})
    writer.writerow({"first_name": "Jane", "last_name": "Smith"})

     