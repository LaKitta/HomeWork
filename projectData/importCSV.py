import sqlite3

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

# fhand = open('sqllab_projectExpense.csv', encoding='utf-8')
fhand = open('sqllab_projectRevenue.csv', encoding='utf-8')

# count = 0

for line in fhand:
    record = line.strip()
    list = record.split(',')
    # cur.execute('INSERT INTO projectExpense VALUES (?,?,?,?,?,?,?)', (list[0],list[1],list[2],list[3],list[4],list[5],list[6]))
    cur.execute('INSERT INTO projectRevenue VALUES (?,?,?,?)', (list[0],list[1],list[2],list[3]))
    
    # count = count + 1

conn.commit()
# if count > 50: break