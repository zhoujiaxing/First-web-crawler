#from bs4 import BeautifulSoup
import urllib2
import urllib

class Download(object):
	def get_comment(self,url):
		response=urllib2.urlopen(url)
		if response.getcode()!=200:
			return None
		comment=response.read()
		return comment
