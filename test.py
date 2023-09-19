import csv

def read_csv(path):
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter= ";")
      total = [int(row[1]) for row in reader]
   return sum(total)

response = read_csv('./data.csv')
print(response)

