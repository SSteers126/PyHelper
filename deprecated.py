# from gps3 import gps3
# the_connection = gps3.GPSDSocket()
# the_fix = gps3.Fix()

# try:
#     for new_data in the_connection:
#         if new_data:
#             the_fix.refresh(new_data)
#         if not isinstance(the_fix.TPV['lat'], str): # lat as determinate of when data is 'valid'
#             speed = the_fix.TPV['speed']
#             latitude = the_fix.TPV['lat']
#             longitude = the_fix.TPV['lon']
#             altitude  = the_fix.TPV['alt']
#             # etc....
#             print(latitude)
#             print(longitude)
# except:
#     print("error")

# w = observation.get_weather()
# wind = w.get_wind()
# print(w, wind)

# import geocoder
# g = geocoder.ip('me')
# print(g.latlng)

# proxy_support = urllib3.ProxyHandler({"http":"http://66.102.7.4:80"})
# # proxy_support = urllib3.ProxyHandler({"http":"http://61.233.25.166:80"})
# opener = urllib3.build_opener(proxy_support)
# urllib3.install_opener(opener)

# html = urllib3.urlopen("http://www.google.com").read()
# print(html)

# print(g.geojson['address']['lat'])
# print(g.geojson['address']['lng'])
# print(g.json)
# print(g.wkt)
# print(g.osm)

# from gps3 import gps3
# gps_socket = gps3.GPSDSocket()
# data_stream = gps3.DataStream()
# gps_socket.connect()
# gps_socket.watch()
# for new_data in gps_socket:
#     if new_data:
#         data_stream.unpack(new_data)
#         print('Altitude = ', altitude := data_stream.TPV['alt'])
#         print('Latitude = ', latitude := data_stream.TPV['lat'])