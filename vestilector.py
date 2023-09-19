import csv

def lector(ruta):
    with open(ruta, "r") as doccsv:
        ellector = csv.reader(doccsv, delimiter = ";")
        cabecero= next(ellector)
        datos= []
        for i in ellector:
            eliterable = zip(cabecero,i)
            dictprenda = {key: value for key,value in eliterable}
            datos.append(dictprenda)
        return datos
 
           
                   
            
if __name__ == "__main__":
    datos = lector("./vestidorcsvsinUTF8.csv")
    print(datos[10])
    print(type(datos))
 
 