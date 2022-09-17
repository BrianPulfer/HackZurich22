from bs4.element import Comment

unwanted_things = ["style", "script", 'head', "title", "meta", "[document]"]


def remove_unwanted(element):
    # Function from:
    # https://stackoverflow.com/questions/1936466/how-to-scrape-only-visible-webpage-text-with-beautifulsoup
    if element.parent.name in unwanted_things:
        return False
    if isinstance(element, Comment):
        return False
    return True


def filter_unwanted_stuff(dictionary):
    if len(str(dictionary).split("://")) > 1:
        return True
    if len(str(dictionary).split("@")) > 1:
        return True
    return False

def dict2string(string, dictionary):

    if not isinstance(dictionary, dict) and not isinstance(dictionary, list):
        if filter_unwanted_stuff(dictionary):
            return string
        return f"{string}\n. {str(dictionary)}" 

    if isinstance(dictionary, dict):
        for k in dictionary.keys():
            if k != "link":
                string = dict2string(string, dictionary[k])

    if isinstance(dictionary, list):
        for k in dictionary:
            string = dict2string(string, k)

    return string

def split_string_chunks(string, chunk_size):
    # Function from:
    # https://stackoverflow.com/questions/9475241/split-string-every-nth-character

    return [string[i:i + chunk_size] for i in range(0, len(string), chunk_size)]

def join_chunks_in_strings(chunks, join_word=" ."):
    return join_word.join(chunks)
