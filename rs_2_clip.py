### Description: Scripts to automate catchment delineation             ###
###              Step 2: Reproject and Clip the mosaiced DEM VRT file  ###
### Author: Ramita Sardana (2021MCS2857)                               ###
### Date: August 7, 2022                                               ###

from osgeo import gdal

print("Beginning Catchment...Step 2")

mosaic_dem = "mosaic.vrt"
spatial_resolution = 30 ### SRTM gives elevation in 30m resolution
jamui_kml = "jamui_kml.kml" ## boundary for clipping
projection_jamui = "EPSG:32644" ## WGS - 84 UTM Zone 44 for Jamui
dem_subset_output = "dem_clipped_reprojected.tif"

warp_options = gdal.WarpOptions(cutlineDSName=jamui_kml, 
                                cropToCutline=True,
                                format='GTIFF',
                                dstSRS=projection_jamui,
                                xRes=spatial_resolution,
                                yRes=spatial_resolution)
output_clipped_dem = gdal.Warp(srcDSOrSrcDSTab=mosaic_dem,
                                destNameOrDestDS=dem_subset_output,
                                options = warp_options)
