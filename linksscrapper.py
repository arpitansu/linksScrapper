import requests
from bs4 import BeautifulSoup

urlFromUser="www.twitter.com"
url = ''

def url(urlFromUser=urlFromUser):
	if "http" in urlFromUser[0:4]:
		url = urlFromUser
	else:
		url = "http://" + urlFromUser
	return url


#print url()

def connectToSite():
	conn = requests.get(url())
	return conn

def bsObject():
	content = connectToSite().content
	soup = BeautifulSoup(content, "html.parser")
	return soup

def collectLink():
	soup = bsObject()
	findAllLinks = soup.find_all('a')
	return findAllLinks

def findThisSiteLinks():
	links = collectLink()
	# linkList = []
	file = open('links.txt', 'w')
	for link in links:
		allLink = link.get('href')
		if 'http' in allLink:
			continue
		else:
			fullLink = url() + allLink
			file.write(fullLink)
			file.write("\n"*3)
			file.close
			# linkList.append(fullLink)
			# linkList.append("\n")
	 # return null

findThisSiteLinks()
