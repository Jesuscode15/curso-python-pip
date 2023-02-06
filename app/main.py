import utils
import read_csv
import charts 


def run():
  data = read_csv.read_csv('/home/yisuscode/py-protect/app/data.csv')
  data = list(map(lambda item : item['Continent'] == 'South America', data))
  
  countries = list(map(lambda x: x['Country'], data))
  porcentages = list(map(lambda x: x['Word Population Porcentages'], data))
  charts.generate_pie_chart(countries, porcentages)
  
  country = input('Type country => ')
  print(country)

  result = utils.population_by_country(data, country)
  
 
  if len(result) > 0:
    country = result[0]
    print(country)
    labels,values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'],labels, values)
  
if __name__=='__main__':
  run()



  

