import urllib.request, urllib.parse, urllib.error
import sqlite3
import json
import time

conn = sqlite3.connect('geo.sqlite')
cur = conn.cursor()

# cur.execute('CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)')

api_key = 42
geocode_url = "http://py4e-data.dr-chuck.net/json?"

params = dict()
params['key'] = 42

fhandle = open('where.data')

count = 0
for line in fhandle:
    if count > 100:
        print('100 geocode requested, restart to request more')
        break

    address = line.strip()

    cur.execute('SELECT address FROM Locations WHERE address = ?', (memoryview(address.encode()),))

    try:
        result = cur.fetchone()[0]
        print("Location loaded, skip...")
        continue
    except:
        pass

    params['address'] = address
    url_encode = geocode_url + urllib.parse.urlencode(params)

    geo_socket = urllib.request.urlopen(url_encode)
    socket_result = geo_socket.read().decode()
    print('Retrieving', address, len(socket_result), 'characters')

    count = count + 1

    try:
        js = json.loads(socket_result)
    except:
        print('json can not parse socker_result')
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print('API unavailabel')
        break

        
    cur.execute('INSERT INTO Locations (address, geodata) VALUES (?,?)', (memoryview(address.encode()), memoryview(socket_result.encode())))

    conn.commit()

    # if count % 10 == 0:
        # print('Pausing for 5 seconds..')
        # time.sleep(5)