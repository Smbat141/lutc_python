#!/usr/bin/python3
"""
A Python script to download and play a media file by FTP.
Uses getfile.py, a utility module which encapsulates FTP step.
"""

import getfile
from getpass import getpass

filename = '1MB.zip'

# fetch with utility
getfile.getfile(file=filename,
                site='speedtest.tele2.net',
                dir='.',
                user=('anonymous', getpass('Pswd?')),
                refetch=True)

# rest is the same
if input('Open file?') in ['Y', 'y']:
    from PP4E.System.Media.playfile import playfile

    playfile(filename)
