import re

url = 'http://www.google.com/index.htm'

url2 = re.findall('http.+htm', url)

print(len(url2))
print(url2)