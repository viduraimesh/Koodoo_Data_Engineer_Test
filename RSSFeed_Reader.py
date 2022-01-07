import feedparser
import csv
NewsFeed = feedparser.parse("https://www.europarl.europa.eu/rss/doc/top-stories/en.xml")

with open("Feed_Results.csv","w",newline="") as fo:
    writer=csv.writer(fo)
    writer.writerow([NewsFeed.feed['title']])

    for entry in NewsFeed.entries:
        writer.writerow([entry.title])
