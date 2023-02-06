import csv

def read_csv(path):
  with open(path,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
      return data
      


if __name__=='__main__':
  data = read_csv('./app/data.csv')
  

#vamos a tranformar una lista a diccionario la llave de ese diccionario va hacer el nombre de la columna 

#utilizamos un zip para unir el header con el row que se esta iterando y se crea una tupla 

# generamos un diccionario con diccionaty comprehension y lo creamos a partir de ese iterable

#