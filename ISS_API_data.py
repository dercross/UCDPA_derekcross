# Import requests package
import requests
#The International Space Station is moving at close to 28,000 km/h so its location changes really fast! Where is it right now?
# Assign URL to variable: url
#url = 'http://api.open-notify.org/iss-now.json'
url = 'http://api.open-notify.org/astros.json'
# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
#print(r.text)
json_data = r.json()

# Print each key-value pair in json_data
#for k in json_data.keys():
    #print(k + ': ', json_data[k])

#For loop to list out People on the international Space Station.
for p in json_data['people']:
    print(p['name'])
