#Derek Cross weather API code to show how to import data from API.
#Open-weather api is a community open by requires API keys, setup with my api key.
#Oputout is the

import requests
import json

#Importing weather for my location Kildare, Ireland from open weather API
url = "https://community-open-weather-map.p.rapidapi.com/weather"

#Query parameters - input my location "Kildare, Ireland","lat":"53.0853","lon":"-6.82"
querystring = {"q":"Kildare, Ireland","lat":"53.0853","lon":"-6.82","callback":"test","id":"2172797","lang":"English","units":"metric","mode":"xml, html"}

#API key details
headers = {
    'x-rapidapi-key': "d04bf6eff3msh485cf1280775583p124e0ejsn9b0d7e8ac469",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
# Request data from open weather data
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
data = response.text