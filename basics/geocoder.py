import pandas
from geopy.geocoders import ArcGIS

nom = ArcGIS()
df = pandas.read_csv("supermarkets.csv")
df.set_index("ID", inplace=True)
df["Address"] = df["Address"] + "," + df["City"] + "," + df["State"] + "," + df["Country"]
# n = nom.geocode("24 BholaNath Das Road Lalbagan,Chandannagar,West Bengal,India")
# print("Latitude={},Longitude={} ".format(n.latitude, n.longitude))
df["Coordinates"] = df["Address"].apply(nom.geocode)
df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x is not None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x is not None else None)
print(df)
