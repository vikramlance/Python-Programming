from BeautifulSoup import BeautifulSoup

import urllib2
url = urllib2.urlopen("http://www.python.org")

content = url.read()

soup = BeautifulSoup(content)

links = soup.findAll("a")
