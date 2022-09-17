from data_retriever import process_webpage, join_chunks_in_strings, split_string_chunks
from model.model import summarize, classify, grammar, translations
from model.utils import find_keyword, KEY_WORDS, WORLD_CONTINENTS, WORLD_COUNTRIES

from termcolor import cprint
from tqdm import tqdm
import json


def data_translation(data_chunks, translation):
    new_chunks = []
    for chunk in tqdm(data_chunks):
        new_chunks.append(translations(chunk, translation))
    return new_chunks


def data_summarization(data_chunks, chunks_size):

    while len(data_chunks) > 1:
        print("Iteration ", len(data_chunks))
        new_chunks = []
        for chunk in tqdm(data_chunks):
            new_chunks.append(summarize(chunk)[0]["summary_text"])
        data_chunks = split_string_chunks(
            join_chunks_in_strings(new_chunks), chunk_size=1024
        )

    return summarize(data_chunks)[0]["summary_text"]


def data_correction(text):
    correct_text = []
    for sentence in tqdm(text.split(".")):
        if len(sentence) > 1:
            correct_text.append(grammar(sentence))

    return join_chunks_in_strings(correct_text, join_word=" ")


class Document:

    def __init__(self, url, resume, labels, word_count):
        self.url = url
        self.resume = resume
        self.labels = labels
        self.word_count = word_count

    def get_json(self):
        return json.dumps({
            "url": self.url,
            "resume": self.resume,
            "labels": self.labels,
            "word_count": self.word_count,
        })

def analyze_website(url, format="xml", chunks_size=1024, translation=None):

    cprint("Downloading the data", "magenta", "on_grey")
    data_chunks = process_webpage(url, format, chunks_size=chunks_size)
    print("Raw data:", data_chunks)

    if translation is not None:
        cprint(f"Apply translation: {translation}", "magenta", "on_grey")
        data_chunks = data_translation(data_chunks, translation)
        print("Translate data:", data_chunks)

    cprint("Resuming the data", "magenta", "on_grey")
    summarization = data_summarization(data_chunks, chunks_size=chunks_size)
    print("Resume:", summarization)

    cprint("Grammar correction", "magenta", "on_grey")
    summarization = data_correction(summarization)
    print("Text corrected:",summarization )

    cprint("Classification", "magenta", "on_grey")
    output = classify(summarization)
    labels = list(zip(output["labels"], output["scores"]))
    print("Labels found", labels)

    cprint("Word counting", "magenta", "on_grey")
    original = join_chunks_in_strings(data_chunks)

    key_words = find_keyword(KEY_WORDS, original)
    continents = find_keyword(WORLD_CONTINENTS, original)
    countries = find_keyword(WORLD_COUNTRIES, original)

    print(" - Key words:", key_words)
    print(" - Continents:", continents)
    print(" - Countries:", countries)

    return Document(
        url=url,
        resume=summarization,
        labels=labels,
        word_count= {
            "key words": key_words,
            "continents": continents,
            "countries": countries,
        }
    )
