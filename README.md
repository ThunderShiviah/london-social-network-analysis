
The directory web_subscriptions contains a scraper for the British Subscription List found at [this link](http://digital.lib.ucdavis.edu/projects/bwrp/Works/LyonEMisce.htm).

The scraper can be run by navigating to the topmost directory level of this project and typing

''' Python
scrapy crawl lyon_emma_list.py -o example.json
'''

See the scrapy [documentation](http://doc.scrapy.org/en/0.24/) for the different output types.
