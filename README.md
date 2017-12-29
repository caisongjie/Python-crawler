Description of the four independent files:
	
	simplecrawler.py: 
	- a simple python web crawler using the requests package and lxml.etree package(XPath). It will write all texts from the target website to a local document file.

	AWS_beginner.py:
	- crawl specific fields on subpages from a catelog page.
	
	download_crawler.py: 
	- The target is a catalog page which has links to different subpages. 
	- This crawler will firstly get to the catalog page and then traverse all the subpages to download the document file on those subpages. The document files are stored in a local directory.

	Traveral.py: 
	- This is not a web crawler. 
	- The program will traverse all the document files in a specific directory and rename them according to some specific keywords in those files.

	webcrawler.py: 
	- This web crawler use PhantomJS + Selenium to simulate brower access to websites. 
	- Since some texts are rendered with Javascripts and simple crawler cannot access those texts directly, though you can see those texts with your brower.
	- The content will be stored in MySQL database if the process is successful.
