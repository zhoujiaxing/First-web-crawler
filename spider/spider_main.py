#from manager import Manager
#from parse import Parse
#from download import Download
#from output import Output
import manager,parse,download,output

class SpiderMain(object):
	def __init__(self):
		self.manager=manager.Manager()
		self.download=download.Download()
		self.parse=parse.Parse()
		self.output=output.Output()
	def craw(self,url):
		self.manager.add_new_url(url)
		count=1
		while self.manager.has_new_url() :
			try:
				url=self.manager.get_new_url()
				comment=self.download.get_comment(url)	
				urls=self.parse.get_urls(comment,url)
				#print "1:%d"%(count)
				self.manager.add_new_urls(urls)
				#print 2
				data=self.parse.get_data(url,comment)
				#print data['url']
				self.output.add_data(data)
				#print 4
				print "add to output %dth:%s"%(count,url)
				#count=count+1
				#if count==10 : 
				#	break
			except: print "Parse Filed"
			count=count+1
			if count==1000 :
				break
		self.output.print_html()
if __name__=="__main__":
	url="http://baike.baidu.com/view/125370.htm"
	spider_test=SpiderMain()
	spider_test.craw(url)
	
