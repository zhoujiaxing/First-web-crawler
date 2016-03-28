import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Output(object):
	def __init__ (self):
		self.datas=[]
	def add_data(self, data):
		#print self.datas
		if data is None : 
			return 
		#print data['url']
		try:
			self.datas.append(data)
		except:
			print "output"
	def print_html(self):
		flag='\"'
		file1=open("baike.html","w")
		file1.write("<html>")
		file1.write("<body>")
		file1.write("<meta charset=")
		file1.write(flag)
		file1.write("UTF-8")
		file1.write(flag)
		file1.write(">")
		file1.write("<table>")
		for data in self.datas:
			file1.write("<tr>")
                        file1.write("<td>")
			file1.write(data['url'])
                        file1.write("</td>")
                        file1.write("<td>")
			file1.write(data['title'])
                        file1.write("</td>")
                        file1.write("<td>")
			file1.write(data['info'])
                        file1.write("</td>")
                        file1.write("</tr>")

                file1.write("</table>")
		file1.write("</body>")
		file1.write("</html>")

		file1.close();
		#for data in self.datas:
		#	print data['url']
		#	print data['title']
		#	print data['info']
		#	
