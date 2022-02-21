# %%
import requests
import json


with open('countries_info.json', 'r') as f:
    countries = json.load(f)

ls = ','.join([country for country in countries])
url = f'https://disease.sh/v3/covid-19/historical/{ls}?lastdays=360'
data = requests.get(url)
data = json.loads(data.text)

# %%
output = {}
for country in data:    
    if country:
        try:
            country_name = country['country']
            output[country_name] = {
                'cases': country['timeline']['cases'],
                'deaths': country['timeline']['deaths']
            }
        except (ValueError, KeyError):
            continue       


# %%
with open('countries_info.json', 'w') as f:
    json.dump(countries, f, indent=4)



