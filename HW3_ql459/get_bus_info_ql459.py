from __future__ import print_function
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import json
import csv

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python get_bus_info.py <MTA_CODE> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()
mta_code = sys.argv[1]
bus_line = sys.argv[2]
csv = sys.argv[3]
#read data from url
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + mta_code + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

num_bus = len(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

fout = open(csv, "w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")
for i in range(num_bus):
	    bus_latitude = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
	    bus_longitude = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	    try:
	    	stop = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
	    except LookupError:
	    	stop = 'N/A'

	    try:
	    	status = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
	    except LookupError:
	    	status = 'N/A'

	    fout.write("%s,%s,%s,%s\n" %(bus_latitude, bus_longitude, stop, status))
fout.close()