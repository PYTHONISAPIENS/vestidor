import csv 
import functools


def lectorcontador(ruta):
    total = 0
    with open(ruta, "r") as doccsv:
        lector = csv.reader(doccsv, delimiter=";")
        for row in lector:
            total += int(row[10])
    return total

gastototal = lectorcontador("./vestidorcsvsinUTF8.csv")
print(gastototal)
