from bs4 import BeautifulSoup

# import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://www.dr-chuck.com/page1.htm'
# html = urllib.request.urlopen(url).read()

soup = BeautifulSoup('<a href="google.com">google</a>', 'html.parser')

tags = soup('a')

for tag in tags:
    print(tag.get('href', None))