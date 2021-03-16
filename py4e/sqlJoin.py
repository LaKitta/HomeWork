import json
import sqlite3

conn = sqlite3.connect('new.db')
cur = conn.cursor()

# test db connection
# result = cur.execute('SELECT * FROM User')
# row = cur.fetchone()

# push data from dataForDb.json to new.db
json_str = open('dataForDb.json').read()
data_json_str = json.loads(json_str)

for record in data_json_str:
    # print(record[0],type(record[2]))
    # break
    user = record[0]
    course = record[1]
    role = record[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (user,))
    cur.execute('SELECT id FROM User WHERE name = ?', (user,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (course,))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Member (course_id, user_id, role) VALUES (?,?,?)', (course_id, user_id, role,))

    conn.commit()





'''
for row in result:
    print(row[0], row[1])
'''