### Description: Scripts to automate catchment delineation                  ###
###              Step 3: Convert clipped DEM tif file to PCRaster format    ###
### Author: Ramita Sardana (2021MCS2857)                                    ###
### Date: August 7, 2022                                                    ###

from osgeo import gdal, gdalconst

print("Beginning Catchment...Step 3")

clipped_dem_src = "dem_clipped_reprojected.tif"

clipped_dem_dest = "clipped_dem.map"

input = gdal.Open(clipped_dem_src)
output = gdal.Translate(clipped_dem_dest, input, 
                        format="PCRaster",
                        outputType = gdalconst.GDT_Float32,
                        metadataOptions = "VS_SCALAR")

output = None ### write to disk
