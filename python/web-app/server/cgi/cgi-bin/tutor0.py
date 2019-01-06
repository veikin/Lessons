#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()
print('Content-type: text/html')

html = """
<title>tutor0.py</title>
<h1>Greetings</h1>
<hr>
<p>%s</p>
<hr>"""

if not 'user' in form:
    print(html % 'Who are you?')
else:
    print(html % ('Hello, %s.' % form['user'].value))
