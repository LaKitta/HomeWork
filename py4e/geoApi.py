import json
import urllib.request, urllib.parse, urllib.error

api_key = 42
serviceUrl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('input address to query')

    params = {'address':address, 'key':api_key}

    url = serviceUrl + urllib.parse.urlencode(params)

    handle = urllib.request.urlopen(url)

    recev = handle.read().decode()

    recevJson = json.loads(recev)

    lat = recevJson['results'][0]['geometry']['location']['lat']
    lng = recevJson['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = recevJson['results'][0]['formatted_address']
    print(location)

