import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('new.db')
cur = conn.cursor()

itunes_xml = ET.parse('Library.xml')
tracks = itunes_xml.findall('dict/dict/dict')
print('Dict count', len(tracks))

def lookup(track, key):
    found = False
    for child in track:
        if found == True: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

# ite  = 50

for track in tracks:
    # if ite < 0: break

    artist = lookup(track, 'Artist')
    genre = lookup(track, 'Genre')
    album = lookup(track, 'Album')
    title = lookup(track, 'Name')
    length = lookup(track, 'Total Time')
    rating = lookup(track, 'Rating')
    count = lookup(track, 'Play Count')

    if title is None or artist is None or album is None or genre is None:
        continue

    # str1 = str(ite) + 'Inserting, title: ' + title + ', album: ' + album + ', artist: ' + artist
    # print(str1)
    # ite = ite - 1

    cur.execute('INSERT OR IGNORE INTO Artists (name) VALUES (?)', (artist,))
    cur.execute('INSERT OR IGNORE INTO Album (album) VALUES (?)', (album,))
    cur.execute('INSERT OR IGNORE INTO Genre (genre) VALUES (?)',(genre,))

    cur.execute('SELECT id FROM Album WHERE album = ?', (album,))
    album_id = cur.fetchone()[0]
    cur.execute('SELECT id FROM Genre WHERE genre = ?', (genre,))
    genre_id = cur.fetchone()[0]
    cur.execute('SELECT id FROM Artists WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT INTO Track (title, artist_id, album_id, genre_id, len, rating, count) VALUES (?,?,?,?,?,?,?)', (title, artist_id, album_id, genre_id, length, rating, count)) 

    conn.commit()






