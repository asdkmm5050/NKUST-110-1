import branca
import random
import folium
import json

color_scale = branca.colormap.linear.YlOrRd_09.scale(0, 22)  # color scale
taiwan_map = folium.Map(location=[25.0431, 121.539723], zoom_start=7, tiles='Stamen Toner')

cities = json.load(open('./data/twCounty2010.geo.json', encoding='utf-8'))
folium.Choropleth(
    geo_data=cities,
    style_function=lambda x: {
        "fillColor": color_scale,
        "fillOpacity": .5,
        "stroke": True
    }
).add_to(taiwan_map)
taiwan_map.save('./html/台灣.html')
