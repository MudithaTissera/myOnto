#!/usr/bin/python2

# get RSS from daily mirror feed

import feedparser

feed = feedparser.parse('http://www.dailymirror.lk/RSS_Feeds/breaking-news')

count = len(feed['entries'])

print "Entries found : " + str(count)

for item in range(count):
	entry = feed['entries'][item]

	print "Title   : " + entry['title'] 
	print "Summary : " + entry['summary'] 
	print "Link    : " + entry['link'] 
	print ""

print "Done"


# keys
# -----
# summary_detail
# published_parsed
# links
# title
# summary
# guidislink
# title_detail
# link
# published
# id

