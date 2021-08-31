#!/usr/bin/python3

import subprocess
from GPSPhoto import gpsphoto

file = 'IMG_hw17.jpg'

all_data = gpsphoto.GPSPhoto('IMG_hw17.jpg').gpsData
coordinates = f"{all_data['Latitude']}';{all_data['Longitude']}'"

out_file = open('coordinates.txt', 'a')
out_file.write('\n')
out_file.write(coordinates)
out_file.close()

run_subprocess = subprocess.Popen(['python3', 'hw16.py'], stdout=subprocess.PIPE)
print(run_subprocess.stdout.read().decode())
