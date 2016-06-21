import os
from itertools import islice

def starthere():
	read_configfile()
	createArticlePage()
    createIndexPage()
	
def createArticlePage():
	# eventually, this below info should be supplied by the config file
	template = open(r'C:\sc\mycode\py\weblogmaker\templates\default.html','r')
	articlesDir = r'C:\sc\mycode\py\weblogmaker\articles'
	siteDir = r"C:\sc\mycode\py\weblogmaker\site"
	templatePage = template.read()
	
	for article in os.listdir(articlesDir):
		with open(articlesDir + '\\' + article,'r') as currFile:
			head = list(islice(currFile, 3))
			body = list(islice(currFile,3,None))
		    
		print "creating article page for ", article, head
		## read header info from article file
		 # firstline: title
		 # secondline: author
		 # rest is body
		articlePage = templatePage.replace('WEBLOGMAKER_TITLE'			, ''.join(head[0]))
		articlePage =  articlePage.replace('WEBLOGMAKER_AUTHOR'			, ''.join(head[1]))
		articlePage =  articlePage.replace('WEBLOGMAKER_DATE'			, article.replace(".txt",""))
		articlePage =  articlePage.replace('WEBLOGMAKER_CENTRALCONTENT'	, ''.join(body))

		## article file creation
		with open(siteDir + "\\" + article.replace(".txt",".html"),'w') as siteFile: 
			siteFile.write(articlePage)

	template.close()
	

def createIndexPage():
	template = open(r'C:\sc\mycode\py\weblogmaker\templates\default.html','r')
	articlesDir = r'C:\sc\mycode\py\weblogmaker\articles'
	siteDir = r"C:\sc\mycode\py\weblogmaker\site"
	templatePage = template.read()
	articlePage = templatePage
	
	items=''
	for article in os.listdir(articlesDir):
		with open(articlesDir + '\\' + article,'r') as currFile:
			head = list(islice(currFile, 3))
			items = items + '<p><a href="'+ article.replace(".txt",".html") +'">' + ''.join(head[0]) + '</a> <br /> by '+ ''.join(head[1:]) +' </p>'
	
	articlePage = templatePage.replace('WEBLOGMAKER_TITLE'			, 'Weblog entries')
	articlePage =  articlePage.replace('WEBLOGMAKER_CENTRALCONTENT'	, ''.join(items))

	with open(siteDir + "\\index.html",'w') as siteFile: 
		siteFile.write(articlePage)

	template.close()

	
if __name__=="__main__":
    #starthere()
	createArticlePage()
	createIndexPage()
	
