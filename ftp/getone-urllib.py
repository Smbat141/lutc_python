#!/usr/bin/python3
"""
A Python script to download a file by FTP by its URL string; use higher-level
urllib instead of ftplib to fetch file;  urllib supports FTP, HTTP, client-side
HTTPS, and local files, and handles proxies, redirects, cookies, and more;
urllib also allows downloads of html pages, images, text, etc.;  see also
Python html/xml parsers for web pages fetched by urllib in Chapter 19;
"""

import os, getpass
import urllib
from urllib.request import urlopen  # socket-based web tools

filename = '1MB.zip'  # remote/local filename
password = getpass.getpass('Pswd?')

remoteaddr = 'ftp://anonymous:%s@speedtest.tele2.net/%s' % (password, filename)

print('Downloading', remoteaddr)

# this works too:
# urllib.request.urlretrieve("ftp://speedtest.tele2.net", filename) # no need username and password

# remotefile = urlopen(remoteaddr)  # returns input file-like object
# localfile = open(filename, 'wb')  # where to store data locally
# localfile.write(remotefile.read())
# localfile.close()
# remotefile.close()
