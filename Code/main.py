import feedparser
import urllib
#import logging

def rssChecker(s,bluhblah):
	rssLen = len(s.entries)
	podLink = s.entries[0].link
	podName = s.entries[0].title

	return (podLink,podName)

def checker(s,bluhblah):
	i = 0
		for line in bluhblah:
			podName = s.entries[i].title
			if podName == line:
				podState = True
			else:
				podState = False
				i += 1


def downloader(podcastUrl,filename,bluhblah):
	fileRetriever = urllib.URLopener()
	try:
		fileRetriever.retrieve(podcastUrl, filename + '.mp3')
		bluhblah.write(filename + "\n")
		bluhblah.close()
	except Exception, e:
		raise e
		#Could throw in some logging here..

if __name__ == '__main__':
	#while True:
		foo = open("bar.txt", "wb")
		podStream = feedparser.parse('http://www.p4.no/lyttesenter/podcast.ashx?pid=330')

		downloader(rssChecker(podStream)[0],rssChecker(podStream)[1],foo)
		#time.sleep(86400) #Sleep for 24 hours. 



#Need class for downloading and class for reading. Reading class is opening feed, identifying if there are new podcasts.


#Downloader class is obviously for downloading. Furthermore, it need to name the podcasts accordingly. Method instead?
#The name shall be derived from entries[i].title

#Problems: Determining if podcasts have been downloaded already. Could read files in download folder, but naming..
