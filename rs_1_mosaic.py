### Description: Scripts to automate catchment delineation ###
###              Step 1: Mosaic the DEM files              ###
### Author: Ramita Sardana (2021MCS2857)                   ###
### Date: August 7, 2022                                   ###

import glob, os
from osgeo import gdal

print("Beginning Catchment...Step 1")

############### Step 1: Get input DEM files from SRTM ###############
current_directory = os.getcwd()
print("current_directory = ", current_directory)

input_files = glob.glob(current_directory + "\*.tif")
print('Input files {}'.format(input_files))

print(f"Num of input files = {len(input_files)}")

############### Step 2: Mosaic input files into a virtual raster ###############
mosaic = gdal.BuildVRT('mosaic.vrt', input_files)
# mosaic.flushCache()  ### # To save the vrt file in hard disk when running in python shell
mosaic = None # To save the vrt file in hard disk through code


