import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
from plyer import notification

url = "https://news.google.com/news/rss"
while True:
	try:
		xml_data = urlopen(url).read()
		urlopen(url).close()

		sp = BeautifulSoup(xml_data, "xml")
		news_list = sp.find_all('item')
		news_list = news_list[0:21] 

		for news in news_list:
			notification.notify(
				title="Top Headlines of Today",
				message = news.title.text + "\n Published on: "+ news.pubDate.text,
				timeout = 4)

			time.sleep(20)
	except Exception as e:
		print("Some exception occured:", e)
	
	time.sleep(1800)
