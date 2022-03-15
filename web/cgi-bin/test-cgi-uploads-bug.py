#!/usr/bin/python3

import cgi, sys, html

print("Content-type: text/html\n")  # HTML form uploads a file
print("<pre>")
sys.stderr = sys.stdout             # route errors to reply page

form = cgi.FieldStorage()           # fails if any incompatible text file uploads

fileinfo = form['clientfile']       # errors in web server console is stderr not set
print(html.escape(fileinfo.value))   # show file if worked