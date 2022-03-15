import sqlite3

conn = sqlite3.connect("sql_db")
curs = conn.cursor()
# tblcmd = 'create table people (name char(30), job char(10), pay int(4))'
# curs.execute(tblcmd)
# rows = [['Tom', 'mgr', 100000], ['Kim', 'adm', 30000], ['pat', 'dev', 90000]]
# curs.execute('insert into people values (?, ?, ?)', ('Bob', 'dev', 5000))
# curs.executemany('insert into people values (?, ?, ?)', rows)
# print(curs.rowcount, sqlite3.paramstyle, sep="&")
# conn.commit()

curs.execute('select * from people')
print(curs.description)
