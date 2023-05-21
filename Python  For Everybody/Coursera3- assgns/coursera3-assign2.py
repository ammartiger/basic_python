# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://py4e-data.dr-chuck.net/comments_1798544.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
count=0
for tag in tags:
    # print(tag)
    # # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    temp=(tag.contents[0])
    temp2=int(temp)
    # print(type(temp))
    count=count + temp2
    # print('Attrs:', tag.attrs)
print(count)