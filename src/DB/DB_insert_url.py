from DB import DataBase

import argparse

parser = argparse.ArgumentParser(description="Insert URL in DB")

parser.add_argument("--url", help="Webpage url", required=True)
parser.add_argument('--format_url', help="html or xml", required=True)
parser.add_argument('--translation', help="if translation required", default="Nope")

args = parser.parse_args()

row = {"url": args.url, "type_document": args.format_url}
if args.translation != "Nope":
    row["translation"] = args.translation

DataBase.insert_row("Trust_sources", row)