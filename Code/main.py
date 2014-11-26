import feedparser
import urllib2

def rssChecker():
	d = feedparser.parse('http://www.p4.no/lyttesenter/podcast.ashx?pid=330')
	feedTitle = d['feed']['title']
	rssLen = len(d.entries)

	return feedTitle,rssLen

def downloader(podcastUrl):
	pass

if __name__ == '__main__':
	print rssChecker()[0]



#Need class for downloading and class for reading. Reading class is opening feed, identifying if there are new podcasts.


#Downloader class is obviously for downloading. Furthermore, it need to name the podcasts accordingly. Method instead?
#The name shall be derived from entries[i].title

#Problems: Determining if podcasts have been downloaded already. Could read files in download folder, but naming..
