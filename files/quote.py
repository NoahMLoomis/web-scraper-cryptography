import urllib.request as req
from myHTMLParser import myHTMLParser
import random as rand

class Quote():
    def __init__(self):
        self.parser = myHTMLParser()
        self.quotes = self.scrape("https://litemind.com/best-famous-quotes/")

    def scrape(self, url):
        with req.urlopen(url) as f:
             for line in list(line.decode("utf-8").strip() for line in f.readlines()):
                self.parser.feed(line)
        return self.parser.quotes

    def get_random_quote(self):
        return rand.choice(self.quotes)
                    
q = Quote()