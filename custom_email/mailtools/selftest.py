"""
###############################################################################
self-test when this file is run as a program
###############################################################################
"""

#
# mailconfig normally comes from the client's source directory or
# sys.path; for testing, get it from Email directory one level up
#
import sys

sys.path.append('..')
from custom_email import mailconfig

print('config:', mailconfig.__file__)

# get these from __init__
from custom_email.mailtools import (MailFetcherConsole, MailFetcher,
                                    MailSender, MailSenderAuthConsole,
                                    MailParser)

# if not mailconfig.smtpuser:
#     sender = MailSender(tracesize=5000)
# else:
#     sender = MailSenderAuthConsole(tracesize=5000)
#
# sender.sendMessage(From=mailconfig.myaddress,
#                    To=[mailconfig.myaddress],
#                    Subj='testing mailtools package',
#                    extrahdrs=[('X-Mailer', 'mailtools')],
#                    bodytext='Here is my source code\n',
#                    attaches=['selftest.py'],
#                    )

# bodytextEncoding='utf-8',          # other tests to try
# attachesEncodings=['latin-1'],     # inspect text headers
# attaches=['monkeys.jpg'])          # verify Base64 encoded
# to='i18n adddr list...',           # test mime/unicode headers


# change mailconfig to test fetchlimit
# fetcher = MailFetcherConsole()
fetcher = MailFetcher()


def status(*args): print(args)


# MY VERSION | show last email
hdrs, sizes, loadedall = fetcher.downloadAllHeaders()
last_email = len(hdrs) - 5
fulltext = fetcher.downloadMessage(last_email).rstrip()
print(fetcher.downloadMessage(last_email).rstrip(), '\n', '-' * 70)
parser = MailParser()
message = parser.parseMessage(fulltext)
ctype, maintext = parser.findMainText(message)
print('Parsed:', message['Subject'])
print(maintext)
input('Press Enter to exit')  # pause if clicked on Windows
# fetcher.deleteMessages([last_email])


# for num, hdr in enumerate(hdrs[:5]):
#     print(hdr)
#     if input('load mail?') in ['y', 'Y']:
#         print(fetcher.downloadMessage(num + 1).rstrip(), '\n', '-' * 70)

# last5 = len(hdrs) - 4
# msgs, sizes, loadedall = fetcher.downloadAllMessages(status, loadfrom=last5)
# for msg in msgs:
#     print(msg[:200], '\n', '-' * 70)
#
# parser = MailParser()
# for i in [0]:  # try [0 , len(msgs)]
#     fulltext = msgs[i]
#     message = parser.parseMessage(fulltext)
#     ctype, maintext = parser.findMainText(message)
#     print('Parsed:', message['Subject'])
#     print(maintext)
# input('Press Enter to exit')  # pause if clicked on Windows
