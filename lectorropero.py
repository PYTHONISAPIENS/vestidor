import csv

def funcion_lector(ruta):
    with open (ruta,"r") as doccsv:
        lector = csv.reader(doccsv, delimiter =',')
        cabecero = next(lector)
        print(cabecero)
        for i in lector:
            el_iterable = zip(cabecero, i)
            print(list(el_iterable))
 #           print("........"*3)
   #         print(i)
            
if __name__ == "__main__":
    funcion_lector ('./ROPERO.csv')

    
