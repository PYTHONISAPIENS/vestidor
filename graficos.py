import matplotlib.pyplot as plt

def generadorgraficos(paises, precios):
  fig, ax = plt.subplots()
  ax.bar(paises,precios)
  plt.show()
  
def grafiredondo (labels, precios):
      fig, ax = plt.subplots()
      ax.pie(precios, labels = labels)
      ax.axis("equal")
      plt.show()
  
if __name__ =="__main__":
  labels = ["colombia", "españa","africa"]
  precios = [2200,4500,3000]
  #generadorgraficos(paises,precios)
  grafiredondo(labels,precios)