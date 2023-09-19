
import csv 
import functools


def lectorcontador(ruta):
    with open(ruta, "r") as doccsv:
        total = sum(int(i[10]) for i in csv.reader(doccsv))
        return total
    
contabiliza = lectorcontador('./vestidorcsvsinUTF8.csv')
print(contabiliza)
