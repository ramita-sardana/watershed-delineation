### Description: Scripts to automate catchment delineation                  ###
###              Step 4: Calculate Flow Direction                           ### 
###              Step 5: Stream delineation                                 ###
###              Step 6: Catchment delineation                              ###
### Author: Ramita Sardana (2021MCS2857)                                    ###
### Date: August 7, 2022                                                    ###

from pcraster import readmap, report, cellvalue
from pcraster import * # readmap, lddcreate, lddcreatedem, report, streamorder, mapmaximum

print("Beginning Catchment...Step 4: Calculate Flow Direction ")
### 1. Remove pits in DEM. Pits are pixels surrounded by only higher pixels.
###    A Catchment can have only one pit i.e. outlet.
###    The other pits need to be filled using Fill Sinks algorithm.
###    In PCRaster, the lddcreate operation will both fill the DEM and derive flow direction.
###    lddcreate takes DEM as input and has 4 args to control the thresholds for the filling algorithm.

dem = readmap("clipped_dem.map")
flow_direction = lddcreate(dem, 1e31, 1e31, 1e31, 1e31)
dem_filled = lddcreatedem(dem, 1e31, 1e31, 1e31, 1e31)

report(flow_direction, "ldd_flow_dir.map") ## To create files on hard disk
report(dem_filled, "dem_filled.map")

print("Beginning Catchment...Step 5: Stream delineation")
strahler_orders = streamorder(flow_direction)
report(strahler_orders, "strahler_stream_orders.map")
 

# just use it to verify the value in aguila
max_strahler_order_map = mapmaximum(strahler_orders) 
## output of mapmaximum is that each pixel gets a maximum value...so we can fetch first pixel's value
max_strahler_order_tuple = cellvalue(max_strahler_order_map, 0, 0)
print(max_strahler_order_tuple) ## gives a tuple output like (10, True)

max_strahler_order_value = max_strahler_order_tuple[0]
print(max_strahler_order_value) ## this gives the final integer value

for order in range(1, max_strahler_order_value+1):
    stream_greater_than_order = ifthen(strahler_orders >= order, boolean(1))
    report(stream_greater_than_order, 'strahler'+ str(order) +'.map')

print("Beginning Catchment...Step 6: Catchments delineation ")

pits = pit(flow_direction) ## Find all the pits 
report(pits, "pits.map")

catchments = catchment(flow_direction, pits)
report(catchments, "catchments.map")