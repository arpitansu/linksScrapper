import requests
from bs4 import BeautifulSoup

# this url from user will get url from the user
urlFromUser="your url here"

#do not play with this
url = ''

# this defwill create name of the text file
def fileNameMaker():
	Name = urlFromUser.split('.')
	fileName = Name[1]
	return fileName

#converting to complete url
def url(urlFromUser=urlFromUser):
	if "http" in urlFromUser[0:4]:
		url = urlFromUser
	else:
		url = "http://" + urlFromUser
	return url


#connecting to the website
def connectToSite():
	conn = requests.get(url())
	return conn

#converting to beautiful soup
def bsObject():
	content = connectToSite().content
	soup = BeautifulSoup(content, "html.parser")
	return soup

#finding links in the website
def collectLink():
	soup = bsObject()
	findAllLinks = soup.find_all('a')
	return findAllLinks

#diiferentiating between the links of same website.
def findThisSiteLinks():
	links = collectLink()
	file = open(fileNameMaker()+".txt", 'w')
	for link in links:
		allLink = link.get('href')
		if 'http' in allLink:
			continue
		else:
			fullLink = url() + allLink
			file.write(fullLink)
			file.write("\n")
			file.close

#removing duplicate url's
def removeSameLinks():
	lines = open(fileNameMaker()+".txt", 'r').readlines()
	lines_set = set(lines)
	out  = open(fileNameMaker()+".txt", 'w')
	for line in lines_set:
	    out.write(line)
			


findThisSiteLinks()
removeSameLinks()
