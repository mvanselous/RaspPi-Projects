import requests
import json

my_api = 'af64bdcad7f048efb6d30053518979a2'

def jprint(raw_data):
    #json.dumps() will convert the raw data into a python string
    data = json.dumps(raw_data,sort_keys=True,indent=4)
    print(data)
    
    #json.load() takes this string (or any written as a JSON string)
    #and converts it into a python object
    data = json.loads(data)
    return data

parameters = {'apiKey':my_api,
              'cuisine':'italian',
              'diet':'primal',
              'equipment':'pan',
              'maxAlcohol':0,
              'number':5
              }
raw_data = requests.get('https://api.spoonacular.com/recipes/complexSearch',
                    params=parameters)
data = jprint(raw_data.json())

result_dict = data['results']
#at this point we have a list of dictionaries for each search result
