import urllib
import re
import cookielib
import mechanize
from time import sleep
import sys

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
# br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

url = 'https://www.facebook.com/'
url2 = 'https://google.com'
regex = '<span class="count"> \S\S\S\S\S'
pattern = re.compile(regex)

response = br.open(url)
br.select_form(nr = 0)
br.form['email'] = 'varun.pemmaraju@gmail.com'
br.form['pass'] = '123sportsrdabest'
# br.form['persistent'] = '[1]'
br.submit()

response2 = br.open(url)
# Or refresh!

htmltext = response2.read()
titles = re.findall(pattern, htmltext)
print htmltext
print titles

for i in xrange(100,0,-1):
    sleep(1)
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()

    # Can you re-read
response3 = br.response2()
htmltext3 = response3.read()
titles = re.findall(pattern, htmltext3)
print htmltext3
print titles
# link = br.follow_link('https://www.facebook.com/?ref=logo')
# htmltext = link.read()
# titles = re.findall(pattern, htmltext)
# print titles

