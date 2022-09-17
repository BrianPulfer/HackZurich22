
from bs4.element import Comment
from bs4 import BeautifulSoup
from datetime import datetime
import xmltodict, json 
import requests

# Auxiliar functions

unwanted_things = ["style", "script", 'head', "title", "meta", "[document]"]
STATUS_OK = 200

def remove_unwanted(element):
    # Function from:
    # https://stackoverflow.com/questions/1936466/how-to-scrape-only-visible-webpage-text-with-beautifulsoup
    if element.parent.name in unwanted_things:
        return False
    if isinstance(element, Comment):
        return False
    return True


def dict2string(string, dictionary):

    if not isinstance(dictionary, dict) and not isinstance(dictionary, list):
        return f"{string}\n. {str(dictionary)}" 

    if isinstance(dictionary, dict):
        for k in dictionary.keys():
            if k != "link":
                string = dict2string(string, dictionary[k])

    if isinstance(dictionary, list):
        for k in dictionary:
            string = dict2string(string, k)

    return string

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
        self.texts = xmltodict.parse(text)
        self.texts = dict2string("", self.texts)

        self.date = str(datetime.now())


# Main functions

def donwload_html(url, handler=BeautyHandler, **kwargs):
    respond = requests.get(url)
    if respond.status_code == STATUS_OK:
        return handler(respond.text, url, **kwargs)
    raise Exception(f"Status respond {respond.status_code}")


def donwload_xml(url, handler=XMLHandler, **kwargs):
    respond = requests.get(url)
    if respond.status_code == STATUS_OK:
        return handler(respond.text, url, **kwargs)
    raise Exception(f"Status respond {respond.status_code}")


print(donwload_xml("https://www.aemet.es/documentos_d/eltiempo/prediccion/avisos/rss/CAP_AFAE_wah_RSS.xml")().text)
#print(donwload_xml("https://www.dwd.de/DWD/warnungen/cap-feed/de/atom.xml")().text)