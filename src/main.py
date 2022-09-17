from data_analyzer import analyze_website

#data_chunks = process_webpage("https://caps.weathersa.co.za/Home/RssFeed", "xml")
#data_chunks = process_webpage("https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-netherlands", "xml")
#data_chunks = process_webpage("https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion", "html")


document = analyze_website("https://caps.weathersa.co.za/Home/RssFeed", "xml")


print(document.get_json())