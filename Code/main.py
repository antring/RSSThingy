import feedparser
import urllib
import os
import time

def rssInfoRunner(stream):
	rssLen = len(stream.entries)
	podLink = stream.entries[0].link
	podName = stream.entries[0].title

	return podLink, podName

def Checker(fu):
	folder = os.walk("E:\Git Prosjekter\RSSThingy\Code")
	epList = []

	for ep in folder:
		epList = ep[2]

	for thing in epList:	
		if thing.find(fu) == 0:
			return True

	return False

def downloader(podcastUrl,filename):
	fileRetriever = urllib.URLopener()
	try:
		fileRetriever.retrieve(podcastUrl, filename + '.mp3')
		f = open('log.txt','a')
		f.write('(+)Downloaded ' + filename + ' - ' + time.asctime(time.localtime(time.time())) + ('\n'))
		f.close()
	except Exception, e:
		f = open('log.txt', 'a')
		f.write('(!)Downloader error ' + e + time.asctime(time.localtime(time.time())) + ('\n'))
		f.close()
if __name__ == '__main__':
	while True:
		podStream = feedparser.parse('http://www.p4.no/lyttesenter/podcast.ashx?pid=330')
		if Checker(rssInfoRunner(podStream)[1]) == False:
			downloader(rssInfoRunner(podStream)[0],rssInfoRunner(podStream)[1])
		time.sleep(86400) #Sleep for 24 hours. 
