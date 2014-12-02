import feedparser
import urllib
import os

def rssInfoRunner(stream):
	rssLen = len(stream.entries)
	podLink = stream.entries[0].link
	podName = stream.entries[0].title

	return podLink, podName

def Checker(fu):
	folder = os.walk("E:\Git Prosjekter\RSSThingy\Code")

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
	except Exception, e:
		raise e

if __name__ == '__main__':
	#while True:
		podStream = feedparser.parse('http://www.p4.no/lyttesenter/podcast.ashx?pid=330')
		if Checker(rssInfoRunner(podStream)[1]) == False:
			downloader(rssInfoRunner(podStream)[0],rssInfoRunner(podStream)[1])
			print 'Downloading ' + rssInfoRunner(podStream)[1]
		#time.sleep(86400) #Sleep for 24 hours. 