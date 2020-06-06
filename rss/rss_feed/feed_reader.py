import requests
import xml.etree.ElementTree as ET
class FeedReader:
    def loadRSS(self):
        '''
        utility function to load RSS feed
        '''
        # create HTTP request response object
        RSS_FEED_URL =  "http://www.hindustantimes.com/rss/topnews/rssfeed.xml" #"https://tech.economictimes.indiatimes.com/rss/startups"
        resp = requests.get(RSS_FEED_URL)
        return resp.content

    def parseXML(self, rss):
        '''
        utility function to parse XML format rss feed
        '''
        # create element tree root object
        root = ET.fromstring(rss)

        # create empty list for news items
        newsitems = []

        # iterate news items
        for item in root.findall('./channel/item'):
            news = {}

            # iterate child elements of item
            for child in item:

                # special checking for namespace object content:media
                if child.tag == '{http://search.yahoo.com/mrss/}content':
                    news['media'] = child.attrib['url']
                else:
                    news[child.tag] = child.text.encode('utf8')
            newsitems.append(news)

            # return news items list
        return newsitems

    def topStories(self):
        '''
        main function to generate and return news items
        '''
        # load rss feed
        rss = self.loadRSS()

        # parse XML
        newsitems = self.parseXML(rss)
        return newsitems

if __name__ == "__main__":
    fr = FeedReader()
    print(fr.topStories())