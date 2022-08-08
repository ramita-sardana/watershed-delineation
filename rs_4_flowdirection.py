### Description: Scripts to automate catchment delineation                  ###
###              Step 4: Calculate Flow Direction                           ###
### Author: Ramita Sardana (2021MCS2857)                                    ###
### Date: August 7, 2022                                                    ###

from osgeo import gdal
from pcraster import readmap, lddcreate, lddcreatedem, report, streamorder

print("Beginning Catchment...Step 4")
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

strahler_orders = streamorder(flow_direction)

report(strahler_orders, "strahler_stream_orders.map")