
from bs4 import BeautifulSoup
from datetime import datetime
import xmltodict, json 
import requests

# Auxiliar functions

from data_retriever.text_processing import remove_unwanted, filter_unwanted_stuff, dict2string

STATUS_OK = 200

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
