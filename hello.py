import requests
import json


with open('countries.json', 'r') as f:
    countries = json.load(f)

ls = ','.join([country for country in countries])
""" url = f'https://disease.sh/v3/covid-19/historical/{ls}?lastdays=360'
data = requests.get(url)
data = json.loads(data.text) """
with open('countries_test.json', 'w') as f:
    json.dump(countries, f, indent=4)