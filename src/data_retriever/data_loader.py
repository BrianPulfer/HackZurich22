
from bs4.element import Comment
from bs4 import BeautifulSoup
from datetime import datetime
import xmltodict, json 
import requests

# Auxiliar functions

unwanted_things = ["style", "script", 'head', "title", "meta", "[document]"]


def remove_unwanted(element):
    # Function from:
    # https://stackoverflow.com/questions/1936466/how-to-scrape-only-visible-webpage-text-with-beautifulsoup
    if element.parent.name in unwanted_things:
        return False
    if isinstance(element, Comment):
        return False
    return True

#  Data structure

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

#  Data  handlers

class IHandler:

    def __init__(self, text, url, **kwargs):
        self.text = None
        self.url = None 
        self.date = None

    def __call__(self):
        return Document(
            date=self.date,
            url=self.url,
            text=self.texts
        )


class BeautyHandler(IHandler):

    def __init__(self, text, url, **kwargs):

        self.texts = self.__process_text(text)
        self.texts = list(filter(remove_unwanted, self.texts))
        self.texts = " ".join(self.texts)
        self.url = url
        self.date = str(datetime.now())

    def __process_text(self, text):
        soup = BeautifulSoup(text, "html.parser")
        return soup.findAll(text=True)


class XMLHandler(IHandler):

    def __init__(self, text, url, **kwargs):

        self.url = url
        self.texts = json.dumps(xmltodict.parse(text))
        self.date = str(datetime.now())


# Main functions

def donwload_html(url, handler=BeautyHandler, **kwargs):
    respond = requests.get(url)
    if respond.status_code == 200:
        return handler(respond.text, url, **kwargs)
    raise Exception(f"Status respond {respond.status_code}")


def donwload_xml(url, handler=XMLHandler):
    respond = requests.get(url)
    if respond.status_code == 200:
        return handler(respond.text, url, **kwargs)
    raise Exception(f"Status respond {respond.status_code}")


print(donwload_xml("https://www.dwd.de/DWD/warnungen/cap-feed/de/atom.xml")().json())