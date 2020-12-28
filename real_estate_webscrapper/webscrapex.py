import request
from bs4 import BeautifulSoup
import pandas
import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/",
                 headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
l = []
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class", "propertyRow"})
for item in all:
    d = {}
    d["Price"] = item.find("h4", {"class", "propPrice"}).text.replace("\n", "").replace(" ", "")
    d["Address"] = item.find("span", {"class", "propAddressCollapse"}).text
    try:
        d["BedSize"] = item.find("span", {"class", "infoBed"}).find("b").text
    except:
        d["BedSize"] = "No Bed"
    try:
        d["Area"] = item.find("span", {"class", "infoSqFt"}).find("b").text
    except:
        d["Area"] = "None"
    try:
        d["FullBath"] = item.find("span", {"class", "infoValueFullBath"}).find("b").text
    except:
        d["FullBath"] = "None"
    try:
        d["HalfBath"] = item.find("span", {"class", "infoValueHalfBath"}).find("b").text
    except:
        d["HalfBath"] = "None"
    for column_group in item.find_all("div", {"class", "columnGroup"}):
        for feature_group, feature_name in zip(column_group.find_all("span", {"class", "featureGroup"}),
                                               column_group.find_all("span", {"class", "featureName"})):
            if "Lot Size" in feature_group.text:
                d["LotSize"] = feature_name.text
    l.append(d)
pandas.DataFrame(l).to_csv("webscapped.csv")
