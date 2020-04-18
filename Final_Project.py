#The goal below is to build a web app that locates the nearest MBTA stop from a given location input 

#-----------------------Part 1----------------------------------------------------------------
import urllib.request
import json
from pprint import pprint
from json import load

MAPQUEST_API_KEY = 'O1gGM8CKRPGplNw9tGa0zLl1GZUIYdsc'
MAPQUEST_BASE_URL = 'http://www.mapquestapi.com/geocoding/v1/address'

url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
f = urllib.request.urlopen(url)

def get_json(url):
    response_data = ...
    return response_data

response_text = f.read().decode('utf-8')
response_data = json.loads(response_text) #steralizing the data
pprint(response_data)

print(response_data["results"][0]["locations"][0]['postalCode']) #call specific pieces of info out

def get_lat_long(place_name):
    place = place_name.replace(' ', '%20')
    url = f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={place}'
    print(url) 
    place_json = get_json(url)
    pprint(place_json)
    lat = place_json[...][...] # modify this so you get the correct latitude
    lon = place_json[...][...] # modify this so you get the correct longitude

    return lat, lon




