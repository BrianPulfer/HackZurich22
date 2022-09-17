from web.monigros.src.DB import DataBase
from data_analyzer import analyze_website

import argparse


parser = argparse.ArgumentParser(description="Process url")
parser.add_argument("--url_id", help="Url id", required=True)
args = parser.parse_args()


url_row = DataBase.select_row("Trust_sources", args.url_id)
print("Row url:", url_row)

document = analyze_website(
    url=url_row["url"],
    format=url_row["type_document"],
    translation=url_row["translation"],
)

row = {
    "url": document.url, 
    "resume": document.resume,
    "labels":document.labels,
    "word_count":document.word_count,
    "Country": url_row["Country"]
}

DataBase.insert_row("Process_url", row)