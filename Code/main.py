import feedparser
import urllib
import os
import re
#import logging

def rssChecker(s):
	rssLen = len(s.entries)
	podLink = s.entries[0].link
	podName = s.entries[0].title

	stuff = []
	folder = os.walk(".")

	for ep in folder:
		#goget = re.search(r'main',ep)
		print ep


	print stuff

	return (podLink,podName)


def downloader(podcastUrl,filename):
	fileRetriever = urllib.URLopener()
	try:
		fileRetriever.retrieve(podcastUrl, filename + '.mp3')
	except Exception, e:
		raise e
		#Could throw in some logging here..

if __name__ == '__main__':
	#while True:
		podStream = feedparser.parse('http://www.p4.no/lyttesenter/podcast.ashx?pid=330')

		rssChecker(podStream)
		#downloader(rssChecker(podStream)[0],rssChecker(podStream)[1])
		#time.sleep(86400) #Sleep for 24 hours. 



#Need class for downloading and class for reading. Reading class is opening feed, identifying if there are new podcasts.


#Downloader class is obviously for downloading. Furthermore, it need to name the podcasts accordingly. Method instead?
#The name shall be derived from entries[i].title

#Problems: Determining if podcasts have been downloaded already. Could read files in download folder, but naming..
