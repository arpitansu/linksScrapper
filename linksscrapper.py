import requests
import sys
from bs4 import BeautifulSoup


#converting to complete url
def url(urlFromUser=sys.argv[1]):	
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

def fileNameMaker():
	Name = url().split('.')
	fileName = Name[1]
	return fileName

#diiferentiating between the links of same website.
def findThisSiteLinks():
	print ("working , wait for some seconds...")
	links = collectLink()
	file = open(fileNameMaker()+".txt", 'a')
	for link in links:
		allLink = link.get('href')
		if 'http' in allLink:
			continue
		else:
			fullLink = url() + allLink
			file.write(fullLink)
			file.write("\n")
			file.close
	return


#removing duplicate url's
def removeDuplicateLinks():
	lines = open(fileNameMaker()+".txt", 'r').readlines()
	lines_set = set(lines)
	out  = open(fileNameMaker()+".txt", 'w')
	for line in lines_set:
	    out.write(line)

			

if __name__ == '__main__':
	findThisSiteLinks()
	removeDuplicateLinks()
	print ("Process completed, Please check %s.txt in the same dir as the programe" %fileNameMaker())