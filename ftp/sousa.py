#!/usr/bin/python3
"""
Usage: sousa.py.  Fetch and play the Monty Python theme song.
This will not work on your system as is: it requires a machine with Internet access
and an FTP server account you can access, and uses audio filters on Unix and your
.au player on Windows.  Configure this and playfile.py as needed for your platform.
"""
# FOR REVIEW ONLY
from getpass import getpass
from getfile import getfile
from playfile.playfile import playfile

file = 'sousa.au'                      # default file coordinates
site = 'ftp.rmi.net'                   # Monty Python theme song
dir  = '.'
user = ('lutz', getpass('Pswd?'))

getfile(file, site, dir, user)         # fetch audio file by FTP
playfile(file)                         # send it to audio player

# import os
# os.system('getone.py sousa.au')      # equivalent command line
