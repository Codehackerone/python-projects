import folium
import pandas


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name=list(data["NAME"])
type=list(data["TYPE"])
map = folium.Map(location=[38.2, -99.1], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el,nm,ty in zip(lat, lon, elev,name,type):
    fg.add_child(
        folium.Marker(location=[lt, ln], popup=folium.Popup("Name: "+nm+"\n"+"Type:"+ty+"\n"+str(el) + " metres", parse_html=True),
                      icon=folium.Icon(color=color_producer(el))))
fgv = folium.FeatureGroup("Population")
fgv.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig')).read(),
                             style_function=lambda x: {
                                 'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange'
                                 if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fg)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Map1.html")
