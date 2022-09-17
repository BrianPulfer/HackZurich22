# HackZürich 2022

Repository for the HackZürich 2022 edition (September 16 - 18, 2022).

## Description

### Start webpage
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

## Data processing
Example of how our system is able to collect and process information with the use of AI.

### Initial data
Fragment of the downloaded data before analyzing. (Original data came from: https://www.dwd.de/DWD/warnungen/cap-feed/de/atom.xml)
"""
.... Gemeinde Wiendorf, Gemeinde Klein Belitz, Gemeinde Kassow, Gemeinde Wardow, Stadt Laage, Gemeinde Kuhs, Stadt Rostock, Gemeinde Zepelin, Gemeinde Ziesendorf, Gemeinde Kritzmow...\n. 2022-09-17T21:53:00Z\n. (Alert) Amtliche WARNUNG vor GEWITTER\n. 2022-09-17T21:52:00Z\n. 2022-09-17T21:52:00Z\n. text\n. Von Nordwesten ziehen Gewitter auf. Dabei gibt es Windböen mit Geschwindigkeiten bis 60 km/h (17m/s, 33kn, Bft 7). - Betroffene Gebiete: Gemeinde Westerstetten, Gemeinde Mühlhausen im Täle, Gemeinde Westerheim, Gemeinde Altheim (Alb), Gemeinde Altheim, Gemeinde K', 'uchen, Gemeinde Allmendingen, Gemeinde Weidenstetten, Gemeinde Bissingen an der Teck, Stadt Göppingen...\n. 2022-09-17T21:52:00Z\n. (Update) Amtliche WARNUNG vor WINDBÖEN\n. 2022-09-17T19:53:00Z\n. 2022-09-17T19:53:00Z\n. text\n. Es treten Windböen mit Geschwindigkeiten bis 60 km/h (17m/s, 33kn, Bft 7) aus nordwestlicher Richtung auf. In Schauernähe sowie in exponierten Lagen muss mit Sturmböen bis 70 km/h (20m/s, 38kn, Bft 8) gerechnet werden. - Betroffene Gebiete: Gemeinde Brinkum, Gemeinde Detern, Gemeinde Holtland, Gemeinde Hesel, Gemeinde Firrel, Gemeinde Filsum, Gemeinde Neukamperfehn, Gemeinde Moormerland, Stadt Leer (Os... 
"""
### Data processed and use in our app
![](overview.png "Final application")


## Authors
[BrianPulfer](https://github.com/BrianPulfer) and [ipmach](https://github.com/ipmach).
