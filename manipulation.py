import csv

cities = [{
    "country": "France",
    "capital": "Paris",
    "weather": 12
}, {
    "country": "Germany",
    "capital": "Berlin",
    "weather": 10
}, {
    "country": "Italy",
    "capital": "Rome",
    "weather": 8
}]

fields_name = ["country", "capital", "weather"]

file_name = 'cities.csv'

#create a file writter
with open(file_name, 'w') as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=fields_name)
  #create the header
  writer.writeheader()
  writer.writerows(cities)

#open the file
with open(file_name, 'r') as csvfile:
  #read the csv file
  reader = csv.DictReader(csvfile)
  for line in reader:
    print(line['country'])
    print(line['capital'])
    print(line['weather'])
