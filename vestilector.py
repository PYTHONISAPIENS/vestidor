import csv

def funcilector (ruta):
    with open(ruta,"r") as docucsv:
        lector = csv.reader(docucsv, delimiter = ";")
        for i in lector:
            print("...."*4)
            print(i)

if __name__ == "__main__":
    funcilector("./vestidor.csv")