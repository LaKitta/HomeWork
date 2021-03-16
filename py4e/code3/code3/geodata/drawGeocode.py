import sqlite3
import json
import codecs

conn = sqlite3.connect('geo.sqllite')
cur = conn.cursor()

fhand = codecs.open('where.js', 'w', 'utf-8')
fhand.write("myData = [\n")

count = 0
row_count = 0

cur.execute('SELECT * FROM Locations')

for record in cur:
    row_count = row_count + 1

    geodata = str(record[1].decode())
    try:
        js = json.loads(str(geodata))
    except:
        continue

    
    try:
        where = js['results'][0]['formatted_address'].replace("'", "")
        #print('Retriving', where)
        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js['results'][0]['geometry']['location']['lng']
    except:
        print(record[0])
        break

    if lat == 0 or lng == 0: continue


    try:
        count = count + 1
        print(where, lat, lng, row_count, count)
        if count > 1: fhand.write(",\n")
        js_item = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(js_item)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()

