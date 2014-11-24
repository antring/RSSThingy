import feedparser

#------------------------------------------
class Reader:
	"""docstring for Reader"""
	def __init__(self,rssfeed):
		self.rss = feedparser.parse(rssfeed)
		self.feedTitle = self.rss['feed']['title']
		self.rssLen = len(self.rss.entries)

	def printshit(self): #for testing only, deleting soon(tm)
		print self.feedTitle
		print self.rssLen

		
#------------------------------------------

class downloader(object):
	"""docstring for downloader"""
	def __init__(self):
		pass

#------------------------------------------

if __name__ == '__main__':
	test = Reader('http://www.p4.no/lyttesenter/podcast.ashx?pid=330')
	Reader.printshit(test)

#Need class for downloading and class for reading. Reading class is opening feed, identifying if there are new podcasts.


#Downloader class is obviously for downloading. Furthermore, it need to name the podcasts accordingly. Method instead?
#The name shall be derived from entries[i].title

#Problems: Determining if podcasts have been downloaded already. Could read files in download folder, but naming..