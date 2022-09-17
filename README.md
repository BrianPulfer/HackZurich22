# HackZürich 2022

Repository for the HackZürich 2022 edition (September 16 - 18, 2022).

## Description

## Start webpage
- To execute the server and interact with the map, execute in the web folder:
``` bash 
  npm start 
```
The map is update it in real after we process a new url.
### DB operations
Commands to interact with the database
- Read tables of the DB
``` bash 
  python DB_read_table.py --name_db NAME_DB
```
- Insert trust url to check information from. The format of the url can be html or xml
``` bash 
  python DB_insert_url.py --url URL --format_url FORMAT --country COUNTRY
```
Also you can add for a translation for the url with the command --translation TRANSLATION. (Only translation available ger_en)

### Process url
Process an url to update the dashboard map. Download the webpage, make a resume and classify its importance. 
``` bash 
  python process_url.py --url_id URL_ID
```
To get the url_id of a specific trust url, you can execute
``` bash 
  python DB_read_table.py --name_db Trust_sources
```
![](overview.png "Final application")

## Authors
[BrianPulfer](https://github.com/BrianPulfer) and [ipmach](https://github.com/ipmach).
