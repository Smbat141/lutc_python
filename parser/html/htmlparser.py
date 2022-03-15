import html
from html.parser import HTMLParser

# class ParsePage(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print('Tag start:', tag, attrs)
#
#     def handle_endtag(self, tag):
#         print('tag end:  ', tag)
#
#     def handle_data(self, data):
#         print('data......', data.rstrip())
#
#
# page = """
# <html>
# <h1>Spam!</h1>
# <p>Click this <a href="http://www.python.org">python</a> link</p>
# </html>"""
#
# parser = ParsePage()
# parser.feed(page)

# print('-' * 40)
#
# print(html.unescape(s))

s = html.escape("1<2 <b>hello & bye</b>")
class Parse(HTMLParser):
    def handle_data(self, data):
        print(data, end='')

    def handle_entityref(self, name):
        map = dict(lt='<', gt='>', amp='&')
        print(map[name])


# print('-' * 40)
from html.entities import entitydefs
# s = html.escape("1<2 <b>hello</b>")
# class Parse(HTMLParser):
#     def handle_data(self, data):
#         print(data, end='')

#     def handle_entityref(self, name):
#         print(entitydefs[name])


P = Parse(convert_charrefs=False)
P.feed(s)
