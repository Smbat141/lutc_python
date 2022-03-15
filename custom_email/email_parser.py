# from email.message import Message
#
# m = Message()
# m['from'] = 'smbatpaloyan@gmail.com'
# m['to'] = 'smbatpaloyan@gmail.com'
# m.set_payload('The owls are not what they seem...')
#
# s = str(m)
# print(s)
#
# print(80 * "-")
#
# from email.parser import Parser
#
# x = Parser().parsestr(s)
# print(x)
# print(x['From'])
# print(x.get_payload())
# print(x.items())
#
# print(80 * "-")
#
# for part in x.walk():
#     print(x.get_content_type())
#     print(x.get_payload())
#
# print(80 * "-")
#
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# top = MIMEMultipart()
# top['from'] = 'Art <arthur@camelot.org>'
# top['to'] = 'PP4E@learning-python.com'
# sub1 = MIMEText('nice red uniforms...\n')
# sub2 = MIMEText(open('/home/collab06/projects/lutc_python/text.txt').read())
# sub2.add_header('Content-Disposition', 'attachment', filename='text.txt')
# top.attach(sub1)
# top.attach(sub2)
# text = top.as_string()
# print(text)
#
# print(80 * "-")
#
# msg = Parser().parsestr(text)
# for part in msg.walk():
#     print(part.get_content_type())
#     print(part.get_payload())
#     print()
#
# print(80 * "-")
#
# btext = text.encode()
# # msg = Parser().parsestr(btext) # throw exception
# msg = Parser().parsestr(btext.decode()) # ok
# print(msg)
########################################################################################################################

# from email.message import Message
#
# m = Message()
# m['From'] = 'Lancelot'
# m.set_payload('Line?...')
# print(m.get_payload())
# print(m.get_payload(decode=True))
# print(m.get_payload(decode=True).decode())

########################################################################################################################
# from email.message import Message
#
# s = b'A\xe4B'
# s.decode('latin1')
#
# m = Message()
# m.set_payload(b'A\xe4B', charset='latin1')
# t = m.as_string()
# print(t)
# print(m.get_content_charset())
# # print(m.get_payload(decode=True).decode())  # throw exception
# print(m.get_payload(decode=True).decode('latin1'))  # throw exception

########################################################################################################################
# rawheader = '=?UTF-8?Q?Introducing=20Top=20Values=3A=20A=20Special=20Selection=20of=20Great=20Money=20Savers?='
#
# from email.header import decode_header
#
# print(decode_header(rawheader))
# bin, enc = decode_header(rawheader)[0]
# print(bin, enc, sep="&&")
# print(bin.decode(enc))
########################################################################################################################
# from email.utils import parseaddr, formataddr
# p = parseaddr('"Smith, Bob" <bob@bob.com>')
# print(formataddr(p))
# print(parseaddr('Bob Smith <bob@bob.com>'))
# print(formataddr(parseaddr('Bob Smith <bob@bob.com>')))
# print(parseaddr('bob@bob.com'))
# print(formataddr(parseaddr('bob@bob.com')))
########################################################################################################################
# multi = '"Smith, Bob" <bob@bob.com>, Bob Smith <bob@bob.com>, bob@bob.com, "Bob" <bob@bob.com>'
# print(getaddresses([multi]))
# print([formataddr(pair) for pair in getaddresses([multi])])
# print(', '.join([formataddr(pair) for pair in getaddresses([multi])]))
# print(getaddresses(['bob@bob.com']))
########################################################################################################################
# from email.header import make_header, decode_header
# hdr = make_header([(b'A\xc4B\xe4C', 'latin-1')])
# print(hdr)
# print(hdr.encode())
# print(decode_header(hdr.encode()))
########################################################################################################################
# from email.header import Header
# h = Header(b'A\xe4B\xc4X', charset='latin-1')
# print(h.encode())
# h = Header('spam', charset='ascii')
# print(h.encode())
########################################################################################################################
# from email.message import Message
# m = Message()
# m['From'] = 'bob@bob.com'
# m.set_payload(open('/home/collab06/projects/lutc_python/text.txt').read())
# print(m)
########################################################################################################################
# from email.message import Message
# m = Message()
# m['From'] = 'bob@bob.com'
# bytes = open('/home/collab06/projects/lutc_python/9780596158118/PP4E-Examples-1.4/Examples/PP4E/Gui/PIL/images/dublin-2010.jpg', 'rb').read()
# m.set_payload(bytes)
# print(m)
########################################################################################################################
# from email.mime.image import MIMEImage
# bytes = open('/home/collab06/projects/lutc_python/9780596158118/PP4E-Examples-1.4/Examples/PP4E/Gui/PIL/images/dublin-2010.jpg', 'rb').read()
# m = MIMEImage(bytes)
# print(type(m))
# print(m.get_payload()[:40])
########################################################################################################################
# from email.mime.text import MIMEText
# m = MIMEText('abc', _charset='ascii')
# m = MIMEText('abc', _charset='latin1')
# m = MIMEText(b'abc', _charset='latin1')
# m = MIMEText(b'A\xe4B', _charset='latin1')
# m = MIMEText(b'A\xe4B', _charset='latin-1')
# print(m)
########################################################################################################################
from email.message import Message
from email.mime.text import MIMEText

# m = Message()
# m.set_payload('spam', charset='us-ascii')
# print(m)
# m = Message()
# m.set_payload(b'spam', charset='us-ascii')
# print(m)

m = Message()
m.add_header('Content-Type', 'text/plain')
m['MIME-Version'] = '1.0'
m.set_param('charset', 'us-ascii')
m.add_header('Content-Transfer-Encoding', '7bit')
data = 'spam'
# data = b'spam'
m.set_payload(data.decode('ascii'))
print(m)
