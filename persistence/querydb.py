"""
run a query string, display formatted result table
example: querydb.py sql_db "select name, job from people where pay > 50000"
"""

import sys

database, querystr = 'sql_db', 'select * from people'
if len(sys.argv) > 1: database = sys.argv[1]
if len(sys.argv) > 2: querystr = sys.argv[2]

from makedicts import makedicts
from dumpdb import showformat
from loaddb import login

conn, curs = login(database)
rows = makedicts(curs, querystr)
showformat(rows)
