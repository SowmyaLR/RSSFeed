import feedparser

res = feedparser.parse('https://timesofindia.indiatimes.com/rssfeedstopstories.cms')
print(res['feed'])