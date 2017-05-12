# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib.request import urlopen
from contextlib import contextmanager

def changeList(attrs):
    refs={}
    for x,y in attrs:
        refs[x]=y
    return refs

class MyHTMLParser(HTMLParser):

    findul=False
    show=False

    def handle_starttag(self, tag, attrs):
        attrs=changeList(attrs)
        if 'class' in attrs and attrs['class']=='list-recent-events menu':
            self.findul=True
        
        if tag=='time' and  'datetime' in attrs:
            self.show=True
        elif tag=='a':
            self.show=True
        elif tag=='span' and 'class' in attrs and  attrs['class']=='event-location':
            self.show=True
        #print(attrs)

    def handle_endtag(self, tag):
        if self.findul==True and  tag=='ul':
            self.findul=False

    def handle_data(self, data):
        if self.findul==True and  self.show==True:
            print(data.strip())


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
        
parser = MyHTMLParser()
with closing(urlopen('https://www.python.org/events/python-events/')) as page:
    parser.feed(page.read().decode('utf-8'))
    
