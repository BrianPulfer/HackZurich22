import pandas as pd
import json 

# DB constans
conf_file = "web/monigros/src/DB/DB_files/conf.json"
tables_conf_file = "Tables"
table_name_conf = "Name_table"
primary_key_conf = "Primary_key"
prefix_id_conf = "Prefix_id"

# Util functions
def read_json_files(path):
    with open(path) as json_file:
        data = json.load(json_file)
    return data

def write_json_files(path, json_file):
    print(json_file)
    with open(path, "w") as f:
        f.write(json_file)

# Main database
class DataBase:

    @staticmethod
    def __get_config_info(conf_field):
        return read_json_files(conf_file)[conf_field]

    @staticmethod
    def read_table(table_name):
        tables = DataBase.__get_config_info(tables_conf_file)
        try:
            data = read_json_files(tables[table_name][table_name_conf])
        except KeyError:
            raise Exception(f"Table {table_name} not found")
        return pd.DataFrame(data)

    @staticmethod
    def select_row(table_name, primary_key):
        table = DataBase.read_table(table_name)
        id_column = DataBase.__get_config_info(
            tables_conf_file
        )[table_name][primary_key_conf]
        return table[table[id_column] == primary_key].iloc[0]

    @staticmethod
    def insert_row(table_name, row):

        # Geting conf info
        table = DataBase.read_table(table_name)
        id_column = DataBase.__get_config_info(
            tables_conf_file
        )[table_name][primary_key_conf]
        id_prefix = DataBase.__get_config_info(
            tables_conf_file
        )[table_name][prefix_id_conf]
        table_path = DataBase.__get_config_info(
            tables_conf_file
        )[table_name][table_name_conf]

        # Inserting
        row[id_column] = f"{id_prefix}{len(table) + 1}"
        table = pd.concat([table, pd.DataFrame([row])])

        # Converting to json
        table = table.to_json(orient="records")
        table = json.loads(table)
        table = json.dumps(table, indent=4)
        
        write_json_files(table_path, table)
        print("Insertion went OK")

