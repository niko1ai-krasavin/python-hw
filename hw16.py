#!/usr/bin/python3

from geopy.geocoders import Nominatim

file1 = open("coordinates.txt", "r")
print('Output data:')
while True:
    line = file1.readline()
    if not line:
        break
    coordinates = line.replace('\'', '').replace(';', ',')
    geo_locator = Nominatim(user_agent="Nikolai-project")
    location = geo_locator.reverse(coordinates)
    url = "https://www.google.com/maps/search/?api=1&query=" + coordinates
    print('Location: ', location)
    print('Goggle Maps URL: ', url)
file1.close()
