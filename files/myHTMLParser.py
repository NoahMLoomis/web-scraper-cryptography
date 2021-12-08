from html.parser import HTMLParser
import re

class myHTMLParser(HTMLParser):

    def __init__(self):
        self.is_quote = False
        self.quotes = []
        super().__init__()
        self.reset()

    def handle_starttag(self, tag, attrs):
        self.is_quote = False
        for att in attrs:
            if att[0] == "class" and att[1] == "wp_quotepage_quote":
                self.is_quote = True

    def handle_data(self, data):
        if self.is_quote:
            self.quotes.append(re.sub(r'^[\d.-]+\s*', '', data.upper()))
