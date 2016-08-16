import csv

a = list()
with open("/home/iraqez/agro2012.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        a.append(row[0])

print(a)