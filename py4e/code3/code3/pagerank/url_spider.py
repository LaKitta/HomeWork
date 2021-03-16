from bs4 import BeautifulSoup
import sqlite3
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# initiate

start_url = 'http://xiedongfeng.com/'
# start_url = 'http://www.dr-chuck.com'


cur.execute('INSERT OR IGNORE INTO Webs (url) VALUES (?)', (start_url,))
cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES (?, NULL, 1.0)', (start_url,))

conn.commit()

# Get all urls from DB 

cur.execute('SELECT url FROM Webs')
webs = list()
for url in cur:
    webs.append(str(url[0]))

steps = 1000
while True:
    if steps < 0: break
    steps = steps - 1

    cur.execute('SELECT id, url FROM Pages WHERE html is NUll AND error is NULL ORDER BY RANDOM() LIMIT 1')

    try:
        row = cur.fetchone()
        fromid = row[0]
        url = row[1]
    except:
        print('Spider finished')
        break

    # Delete all records for current from_url
    cur.execute('DELETE FROM Links WHERE from_id=?', (fromid,))

    # Store text/html into Pages
    try:
        document = urllib.request.urlopen(url, context=ctx)
        if document.getcode() != 200:
            print('Error while open page', document.getcoed())
            cur.execute('UPDATE Pages SET error=? WHERE url=?', (document.getcode(), url))
            continue

        if document.info().get_content_type() != 'text/html':
            print('Ignore non text/html Pages')
            cur.execute('UPDATE Pages SET error=-2 WHERE url=?', (url,))
            continue

        print('Start parsing page...')
        html = document.read()
        soup = BeautifulSoup(html, 'html.parser')
    except:
        print('Somehow unable to retrive or parse page')
        cur.execute('UPDATE Pages SET error=-1 WHERE url=?', (url,))
        conn.commit()
        continue

    cur.execute('UPDATE Pages SET html=? WHERE url=?', (memoryview(html), url))
    conn.commit()

    # Retrive all anchor tags
    tags = soup('a')
    count = 0
    for tag in tags:
        href = tag.get('href', None)
        if href is None or len(href) < 1: continue
        # fix relative url, # section, jpg`png`gif
        up = urllib.parse.urlparse(href)
        if len(up.scheme) < 1:
            href = urllib.parse.urljoin(url, href)
        ipos = href.find('#')
        if ipos > 1: href = href[:ipos]
        if href.endswith('.png') or href.endswith('.jpg') or href.endswith('gif'): continue
        if href.endswith('/'): href = href[:-1]

        found = False
        for web in webs:
            if (href.startswith(web)):
                found = True
                break

        # ensure only spider links with in DB.Webs range
        if not found: continue

        cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES (?, NULL, 1.0)', (href,))
        conn.commit()

        try:
            cur.execute('SELECT id FROM Pages WHERE url=?', (href, ))
            toid = cur.fetchone()[0]
        except:
            continue

        cur.execute('INSERT OR IGNORE INTO Links (from_id, to_id) VALUES (?,?)', (fromid, toid))
        count = count + 1
        conn.commit()

    print('Retrive', count, 'urls from this page', url)

cur.close()