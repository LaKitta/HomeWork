# GET http://www.dr-chuck.com/page1.htm HTTP/1.0

# http://xiedongfeng.com/#/login?redirect=%2Fabout
# nmap -sC -sV {{address_or_addresses}}

"""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)) < 1:
        break
    print(data.decode())

mysock.close()
"""

# urllib

import urllib.request, urllib.parse, urllib.error
import re

url = 'http://www.dr-chuck.com/page1.htm'
n = 0


while n < 5:
    handle = urllib.request.urlopen(url)
    for line in handle:
        lineDecoded = line.decode().strip()
        print(lineDecoded)
        extraUrl = re.findall('http.+htm', lineDecoded)
        if (len(extraUrl) > 0):
            print('find new url')
            url = extraUrl[0]
    n = n + 1