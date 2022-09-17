from src.data_retriever.data_loader import donwload_html, donwload_xml
from src.data_retriever.text_processing import split_string_chunks, join_chunks_in_strings


download_methods = {"html": donwload_html, "xml": donwload_xml}

def process_webpage(url, method, chunks_size=1024):

    download = download_methods[method](url)().text

    list_text = split_string_chunks(
        string=download, chunk_size=chunks_size
    )
    return list_text