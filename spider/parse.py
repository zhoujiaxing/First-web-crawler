from bs4 import BeautifulSoup
import re
import urlparse
class Parse(object):
	def get_urls(self,comment,page_url):
		soup=BeautifulSoup(comment,'html.parser',from_encoding='utf-8')
		new_urls=set()
		links=soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
		for link in links:
			new_url=link['href']
			url=urlparse.urljoin(page_url,new_url)
			new_urls.add(url)
		return  new_urls
	def get_data(self,url,comment):
		data={}
		data['url']=url
		#<dd class="lemmaWgt-lemmaTitle-title">
		soup=BeautifulSoup(comment,'html.parser',from_encoding='utf-8')
	        #print "Hello"
		#links=soup.find('a',href=re.compile(r"/view/\d+\.htm"))
		#print links['href']
		title=soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
		#print title.get_text()
		
		data['title']=title.get_text()
		info=soup.find('div',class_='lemma-summary')
		print data['title']
		data['info']=info.get_text()
		#print data
		return data	
