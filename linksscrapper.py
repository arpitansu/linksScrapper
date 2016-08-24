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
	try:
		print("\n")
		print ("working , wait for some seconds...\n")
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
	except:
		print("something went wrong\n")
		print("Please check if any file created as %s.txt in the same dir as the program" %fileNameMaker()+"\n")
	return


#removing duplicate url's
def removeDuplicateLinks():
	try:
		lines = open(fileNameMaker()+".txt", 'r').readlines()
		lines_set = set(lines)
		out  = open(fileNameMaker()+".txt", 'w')
		for line in lines_set:
		    out.write(line)
	except:
		print("Duplicate links error : No Links are found in the %s.txt" %fileNameMaker()+"\n")

#conver the links to html file 
def toHtmlFile():
		lines = open(fileNameMaker()+".txt", 'r').readlines()
		out  = open(fileNameMaker()+".html", 'w')
		for line in lines:
		    out.write("<a target='_blank' href="+line+">"+line+"</a><br/></br>")
		print("done")
			
def main():
	findThisSiteLinks()
	removeDuplicateLinks()
	print ("Process completed, Please check %s.txt in the same dir as the programe" %fileNameMaker())

	#html file creator
	print("do you want a html file with links to be created ,press [Y/N] or [y/n], or press enter to get out of here \n")
	userGave = raw_input()
	if userGave == 'Y' or userGave == 'y':
		try:
			toHtmlFile()
		except:
			print("something went wrong while creating %s.html file\n" %fileNameMaker())
	elif userGave == 'N' or userGave == 'n':
		print("Ok if you wish")



if __name__ == '__main__':
	main()

