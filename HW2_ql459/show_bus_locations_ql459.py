from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys

if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python  show_bus_locations.py <MTA_CODE> <BUS_LINE>")
    sys.exit()
mta_code = sys.argv[1]
bus_line = sys.argv[2]
#read data from url
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + mta_code + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

num_bus = len(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
print('Bus Line :' + bus_line)
print('Number of Active Buses :%s'%(num_bus))

for i in range(num_bus):
    bus_latitude = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    bus_longitude = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print('Bus %s is at Latitude %s and Longitude %s'%(i+1, bus_latitude, bus_longitude))
