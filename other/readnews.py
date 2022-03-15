"""
fetch and print usenet newsgroup posting from comp.lang.python via the
nntplib module, which really runs on top of sockets; nntplib also supports
posting new messages, etc.; note: posts not deleted after they are read;
"""
# MY VERSION
showhdrs = ['From', 'Subject', 'Date']
try:
    import sys
    servername, groupname, showcount = sys.argv[1:]
except:
    servername = "news.gmane.io"  # assign this to your server
    groupname = "gmane.comp.python.committers"

# connect to nntp server
print('Connecting to', servername)
import nntplib

connection = nntplib.NNTP(servername)
(reply, count, first, last, name) = connection.group(groupname)
print('%s has %s articles: %s-%s' % (name, count, first, last))

resp, overviews = connection.over((last - 9, last))

for id, over in overviews:
    for hdr in showhdrs:
        print(id, nntplib.decode_header(over[hdr.lower()]))
    print(100 * "-")

