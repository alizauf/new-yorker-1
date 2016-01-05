from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://contest.newyorker.com/').read()
soup = BeautifulSoup(r, 'html.parser')

## this gets the image from the new yorker page
for a in soup.find_all(class_ ="cap"):
	print a.get('src')

