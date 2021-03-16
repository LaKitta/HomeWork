import sqlite3


conn = sqlite3.connect('new.db')

cur = conn.cursor()

sql2 = 'SELECT Track.title, Album.album, Genre.genre, Track.len, Track.rating, Track.count FROM Track JOIN Artists JOIN Album JOIN Genre ON Track.album_id = Album.id AND Track.genre_id = Genre.id LIMIT 20'


for track in cur.execute(sql2):
    print(track)


'''
mailAddress = '1@1'

cur.execute('SELECT count FROM Counts WhERE email = ?', (mailAddress,))
result = cur.fetchone()
result2 = cur.fetchall()

print(type(result))
print(result)
print(type(result2))
print(result2)
'''

# conn.commit()
