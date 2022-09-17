
from bs4.element import Comment
from bs4 import BeautifulSoup
from datetime import datetime
import requests

unwanted_things = ["style", "script", 'head', "title", "meta", "[document]"]

def remove_unwanted(element):
    # Function from:
    # https://stackoverflow.com/questions/1936466/how-to-scrape-only-visible-webpage-text-with-beautifulsoup
    if element.parent.name in unwanted_things:
        return False
    if isinstance(element, Comment):
        return False
    return True

class Document:

    def __init__(self, date, url, text):

        self.text = text 
        self.url = url 
        self.date = date

    def json(self):
        return {
            "url": self.url,
            "date": self.date,
            "text": self.text,
        }

class BeautyHandler:

    def __init__(self, text, url):

        self.texts = self.__process_text(text)
        self.texts = list(filter(remove_unwanted, self.texts))
        self.texts = " ".join(self.texts)
        self.url = url
        self.date = str(datetime.now())

    def __process_text(self, text):
        soup = BeautifulSoup(text, "html.parser")
        return soup.findAll(text=True)

    def __call__(self):
        return Document(
            date=self.date,
            url=self.url,
            text=self.texts
        )

def donwload_html(url, handler=BeautyHandler):
    respond = requests.get(url)
    if respond.status_code == 200:
        return handler(respond.text, url)
    raise Exception(f"Status respond {respond.status}")


