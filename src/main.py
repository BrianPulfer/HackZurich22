from data_analyzer import analyze_website

#data_chunks = process_webpage("https://caps.weathersa.co.za/Home/RssFeed", "xml")
#data_chunks = process_webpage("https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-netherlands", "xml")
#data_chunks = process_webpage("https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion", "html")

url = "https://www.dwd.de/DWD/warnungen/cap-feed/de/atom.xml"
document = analyze_website(url, "xml", translation="ger_en")


print(document.get_json())