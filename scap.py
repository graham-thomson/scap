import time
from timeout import timeout
from urlparse import urlparse
from selenium import webdriver

news_sites = \
["http://reddit.com",
"http://nytimes.com",
"http://theguardian.com",
"http://cnn.com",
"http://bbc.co.uk/news",
"http://huffingtonpost.com",
"http://washingtonpost.com",
"http://indiatimes.com",
"http://news.yahoo.com",
"http://weather.com"]

@timeout(60)
def take_screenshot(url, width=1024, height=768):
	print "[{}] grabbing {}...".format(time.strftime("%Y%m%d_%H%M", time.localtime()), url)
	domain = urlparse(url).netloc
	# depot = DepotManager.get()
	driver = webdriver.PhantomJS()
	driver.set_window_size(width, height)
	driver.get(url)
	time.sleep(1)
	driver.save_screenshot('./screencaps/{}_{}.png'.format(time.strftime("%Y%m%d_%H%M", time.localtime()), domain))
	return None

if __name__ == "__main__":
	for site in news_sites:
		take_screenshot(site)