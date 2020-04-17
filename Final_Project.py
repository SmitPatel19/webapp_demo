#The goal below is to build a web app that locates the nearest MBTA stop from a given location input 

#-----------------------Part 1----------------------------------------------------------------
import urllib.request
import json
from pprint import pprint
from json import load

MAPQUEST_API_KEY = 'O1gGM8CKRPGplNw9tGa0zLl1GZUIYdsc'

url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text) #steralizing the data
pprint(response_data)

print(response_data["results"][0]["locations"][0]['postalCode']) #call specific pieces of info out

#print(load(latLng))

for items in response_data['results']:
    print(items['latLng'])
