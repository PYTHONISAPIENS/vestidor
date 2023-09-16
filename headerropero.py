import csv

def funcion_lector(ruta):
    with open (ruta,"r") as doccsv:
        lector = csv.reader(doccsv, delimiter =';')

        for i in lector:

           
            print("........"*3)
            print(i)
            
if __name__ == "__main__":
    funcion_lector ('./vestidorcsvsinUTF8.csv')

    
