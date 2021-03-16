import sqlite3
import re

conn = sqlite3.connect('new.db')

cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Counts;
CREATE TABLE Counts(email TEXT, count INTEGER)''')

fhandle = open('mbox-short.txt')

for line in fhandle:
    mailAddress_re = re.findall('From ([a-z@.]+)', line)
    if (len(mailAddress_re) > 0):
        mailAddress = mailAddress_re[0]
    else:
        continue

    cur.execute('SELECT count FROM Counts WhERE email = ?', (mailAddress,))
    result = cur.fetchone()
    if result is None:
        cur.execute('INSERT INTO Counts VALUES(?, 1)', (mailAddress,))
    else:
        cur.execute('UPDATE Counts SET count = count +1 WHERE email = ?', (mailAddress,))

    conn.commit()

sql_1 = 'SELECT * FROM Counts ORDER BY count DESC LIMIT 10'

for record in cur.execute(sql_1):
    print(record[0], record[1])


