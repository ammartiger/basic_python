import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url=("http://data.pr4e.org")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

#retrieve all anchor tags
tags=soup('a')
print(tags)
for tag in tags:
    print(type(tag))
    print(tag.get('href',None))