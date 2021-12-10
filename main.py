import folium
import pandas as pd
from folium.plugins import HeatMap

latitude = 22.6
longitude = 120.3

cdata = pd.read_csv('./data/NPA_TD1.csv')
incidents = folium.map.FeatureGroup()
latitudes = list(cdata['Latitude'])
longitudes = list(cdata['Longitude'])
labels = list(cdata['設置地址'])
map = folium.Map(location=[latitude, longitude], zoom_start=10)

for lat, lng, label in zip(latitudes, longitudes, labels):  # 標籤圖
    folium.Marker([lat, lng], popup=label).add_to(map)

# heatdata = cdata[['緯度','經度']].values.tolist()#熱度圖
# HeatMap(heatdata).add_to(map)
map.add_child(incidents)

