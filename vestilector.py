import csv

def funcilector (ruta):
    with open(ruta,"r") as docucsv:
        lector = csv.reader(docucsv, delimiter = ",")
        titulo = next(lector)
        
        for i in lector:
            eliterable=zip(titulo,i)
            print(list(eliterable))

if __name__ == "__main__":
    funcilector("./vestidorcsvsinUTF8.csv")