import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL Cerification Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.py4e.com/'
# url = 'https://www.learnerprivacy.org'

try:
    document = urllib.request.urlopen(url, context=ctx)
    if document.getcode() != 200:
        print('Error while open page', document.getcoed())

    if document.info().get_content_type() != 'text/html':
        print('Ignore non text/html Pages')

    print('Start parsing page...')
    html = document.read()
    soup = BeautifulSoup(html, 'html.parser')
except:
    print('Somehow unable to retrive or parse page')

tags = soup('a')
count = 0
for tag in tags:
    href = tag.get('href', None)
    if href is None or len(href) < 1: continue
    # fix relative url, # section, jpg`png`gif
    up = urllib.parse.urlparse(href)
    if len(up.scheme) < 1:
        href = urllib.parse.urljoin(url, href)
    ipos = href.find('#')
    if ipos > 1: href = href[:ipos]
    if href.endswith('.png') or href.endswith('.jpg') or href.endswith('gif'): continue
    if href.endswith('/'): href = href[:-1]

    print(href)
    count = count + 1

print('Retrive', count, 'urls from this page', url)