from web.monigros.src.DB import DataBase

import argparse

parser = argparse.ArgumentParser(description="Read table in DB")

parser.add_argument("--name_db", help="Trust_sources or Process_url", required=True)

args = parser.parse_args()

url_row = DataBase.read_table(args.name_db)

print("Row url:", url_row)