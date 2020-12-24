from pyowm.owm import OWM
owm = OWM("9518c39f6e436ee5999bbbc8ad707342")
weather_mgr = owm.weather_manager()

import geocoder
gip = geocoder.ip('me')
gipc = gip.country
print(gip.latlng)
print("ip country: " + gip.country)

# from ipregistry import IpregistryClient
#
# client = IpregistryClient("tryout")
# ipInfo = client.lookup()
# print(ipInfo)

g = geocoder.mapbox('Boston, ' + gipc, key="pk.eyJ1IjoiemVzdHl5IiwiYSI6ImNrajJ0MGdpOTNmMDUycm40MmVvMWEzdGUifQ.r51BeCXN_rJjy4PScxn33g")
print(g)
# print(g.geojson)
print(g.geojson['features'][0])
city_info = g.geojson['features'][0]['properties']['address']
city = city_info.split(",")[0]
country = city_info.split(" ")[3]
print(city)
latitude = g.geojson['features'][0]['properties']['lat']
longitude = g.geojson['features'][0]['properties']['lng']

print(latitude, longitude)

one_call = weather_mgr.one_call(lat=latitude, lon=longitude)
# one_call = weather_mgr.one_call(g)
print(one_call.forecast_daily[0].temperature('celsius').get('morn', None))

observation = weather_mgr.weather_at_place(city + "," + country)
testobservation = weather_mgr.weather_at_place("Boston,UK")

# print(observation)

# config_dict = owm.configuration
# print(config_dict)

weather = observation.weather
testweather = testobservation.weather
# weather.status           # short version of status (eg. 'Rain')
print(weather.detailed_status)  # detailed version of status (eg. 'light rain')
print(testweather.detailed_status)  # detailed version of status (eg. 'light rain')

def get_weather(city="Boston", country=gipc):
    geocoded = geocoder.mapbox(city + ", " + country, key="pk.eyJ1IjoiemVzdHl5IiwiYSI6ImNrajJ0MGdpOTNmMDUycm40MmVvMWEzdGUifQ.r51BeCXN_rJjy4PScxn33g")
    latitude = geocoded.geojson['features'][0]['properties']['lat']
    longitude = geocoded.geojson['features'][0]['properties']['lng']
    weather = weather_mgr.one_call(lat=latitude, lon=longitude)
    tempurature = weather.forecast_daily[0].temperature('celsius').get('morn', None)
    weather = weather_mgr.weather_at_place(city + "," + gipc).weather.detailed_status
    return tempurature, weather

print(get_weather())