import feedparser
import logging

from rss.rss_feed.feed_url import Technology


class RSSRead:

    def read_entries(self, link):
        try:
            res = feedparser.parse(link)
            return res['entries']
        except Exception as exe:
            logging.exception(exe)

    def get_data(self, entries):
        result = []
        for entry in entries:
            _data = {}
            _data['link'] = entry['link']
            _data['title'] = entry['title']
            result.append(_data)
        return result

    def construct_data(self):
        data = {}
        for key, value in Technology.TECHNOLOGY_URLS.items():
            entries = self.read_entries(value)
            data[key] = self.get_data(entries)
        return data

if __name__ == "__main__":
    rss = RSSRead()
    print(rss.construct_data())
