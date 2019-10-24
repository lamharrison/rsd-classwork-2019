import requests
import json
import requests
import geopy
from IPython.display import Image

quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "2000-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2018-10-11",
                          "orderby": "time-asc"}
                      )



copy= json.loads(quakes.text)

features = copy['features']
maxValue = 0
location = ''
coord = []
url=''

def request_map_at(lat, long, satellite=True,
                   zoom=10, size=(400, 400)):
    base = "https://static-maps.yandex.ru/1.x/?"

    params = dict(
        z=zoom,
        size=str(size[0]) + "," + str(size[1]),
        ll=str(long) + "," + str(lat),
        l="sat" if satellite else "map",
        lang="en_US"
    )

    return requests.get(base, params=params)

for i in features:
    propertyy = i['properties']
    if propertyy['mag'] > maxValue:
        coord = i['geometry']['coordinates']
        maxValue = propertyy['mag']
        location = propertyy['place']




print(coord)
print('The maximum mag is: '+ str(maxValue) + ' at ' +str(location))
map_png = request_map_at(coord[0], coord[1], zoom=10, satellite=False)
Image(map_png.content)