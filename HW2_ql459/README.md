
# PUI2018 HW 3.
## ASSIGNMENTS:
### Part 1: Delete Data
Screenshot for creating test.csv
---------------------------------
![](https://github.com/qiuyliu/PUI2018_ql459/blob/master/HW2_ql459/creat_test.png)
Screenshot for test.csv
------------------------
![](https://github.com/qiuyliu/PUI2018_ql459/blob/master/HW2_ql459/test_screenshot.png)
Screenshot for removing file
----------------------------
![](https://github.com/qiuyliu/PUI2018_ql459/blob/master/HW2_ql459/remove_file.png)
### Part 2: Read CSV files with pandas and use NYC open data portal
I choose the [2016 Green taxi dataset](https://data.cityofnewyork.us/Transportation/2016-Green-Taxi-Trip-Data/hvrh-b6nb/data) from [NYC Open Data](https://opendata.cityofnewyork.us/). This dataset includes trip records from all trips completed in green taxis in NYC on 12/5/2016. The dataset is provided by Taxi and Limousine Commission (TLC).

The first solution is to download the csv file from portal and use environment varaible to move the csv file into the PUIdata folder. Secondly using pandas to show some columns of data. I choose "total_amount" and "trip_distance" two columns to plot the scatter plot. The relation between "total_amount" and "trip_distance" tends to be the positive correlation.

The second solution to approach to the question is to use NYC Open Data API(extra credit part).I choose the "pickup datetime" column and "fare_amount" and "trip_distance" columns' value, and plot both the columns seperatly to present some changes through out the timeline.

### Part3: Show Bus Location
Here is the script: [show_bus_location_ql459.py](https://github.com/qiuyliu/PUI2018_ql459/blob/master/HW2_ql459/show_bus_locations_ql459.py)

show_bus_locations_ql459.py that takes exactly 2 arguments in the following format:
```
python show_bus_locations.py <MTA_KEY> <BUS_LINE>
```

For example \<BUS_LINE> could be B52:

```
python show_bus_locations.py xxxxx-xxxxx-xxxxx-xxxxx-xxxxx B52
```
SAMPLE OUTPUT:
```
Bus Line :B52
Number of Active Buses :14
Bus 1 is at Latitude 40.69932 and Longitude -73.911268
Bus 2 is at Latitude 40.68744 and Longitude -73.959285
Bus 3 is at Latitude 40.689247 and Longitude -73.9242
Bus 4 is at Latitude 40.687495 and Longitude -73.939171
Bus 5 is at Latitude 40.690428 and Longitude -73.98478
Bus 6 is at Latitude 40.690948 and Longitude -73.920606
Bus 7 is at Latitude 40.687086 and Longitude -73.962427
Bus 8 is at Latitude 40.693866 and Longitude -73.990441
Bus 9 is at Latitude 40.689431 and Longitude -73.982321
Bus 10 is at Latitude 40.687633 and Longitude -73.938014
Bus 11 is at Latitude 40.688298 and Longitude -73.979468
Bus 12 is at Latitude 40.693866 and Longitude -73.990441
Bus 13 is at Latitude 40.685859 and Longitude -73.972912
Bus 14 is at Latitude 40.686263 and Longitude -73.94995
```


### Part4: Get Bus Info
Here is the script: [get_bus_info_ql459.py](https://github.com/qiuyliu/PUI2018_ql459/blob/master/HW2_ql459/get_bus_info_ql459.py)

get_bus_info_ql459.py that takes 3 arguments in the following format:

```
python get_bus_info.py <MTA_CODE> <BUS_LINE> <BUS_LINE>.csv
```
__and output to a CSV file named \<BUS_LINE>.csv__:

```
Latitude,Longitude,Stop Name,Stop Status
40.755489,-73.987347,7 AV/W 41 ST,at stop
40.775657,-73.982036,BROADWAY/W 69 ST,approaching
40.808332,-73.944979,MALCOLM X BL/W 127 ST,approaching
40.764998,-73.980416,N/A,N/A
40.804702,-73.947620,MALCOLM X BL/W 122 ST,< 1 stop away
40.776950,-73.981983,AMSTERDAM AV/W 72 ST,< 1 stop away
40.737650,-73.996626,AV OF THE AMERICAS/W 18 ST,< 1 stop away
```
