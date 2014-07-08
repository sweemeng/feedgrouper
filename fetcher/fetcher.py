__author__ = 'sweemeng'
import feedparser
import requests
import nltk

# TODO: How does the architecture look like
# TODO: Return into a format usable for library
#  TODO: There is a few library, we should check it out.
class Item(object):
    """
    Naive Item for HN item. The reason is the HN only have link and title but not content
    :param title title
    :param link  url for feed
    """
    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.content = None

    def fetch_item(self):
        content = requests.get(self.link)
        self.content = nltk.clean_html(content.text)

# FIXME: This is a memory hog
# TODO: Store result in a db somehow
class Fetcher(object):
    """
    Hackernews feed processor got
    """
    def __init__(self, url):
        self.url = url
        self.feed = feedparser.parse(self.url)

    def fetch(self):
        items = []
        entries = self.feed.entries
        for entry in entries:
            items.append(Item(entry.title, entry.link))
