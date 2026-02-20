---
title: "Offline WMS – Benchmarking raster formats for QField – OPENGIS.ch"
author: "Lucie"
date: "2020-06-09T07:03:00+02:00"
lastmod: "2021-05-18T17:53:52+02:00"
categories:
  - "Processing"
  - "QField"
  - "QGIS"
  - "Scripts"
tags:
  - "qgis.org"
source: "www.opengis.ch/it/2020/06/09/offline-wms-benchmarking-raster-formats-for-qfield/index.html"
---

## What are we looking for?
We would like to use WMS offline on QField. For that, we need to figure out what is the best way to get a raster from a WMS and which format is the most efficient (size and performance).
In this post we’ll show you is how to generate the ideal raster file from a WMS and the results of our efficiency tests for the the different raster formats.
## WMS to GPKG
### The simple way
If there is no limitation on the WMS or you need only a small region, here is the easiest process.
  1. Request the WMS and store a [description file in XML](<https://gdal.org/drivers/raster/wms.html#xml-description-file>):


    
    gdal_translate "WMS:url" file.xml -of WMS
  2. Create a Geopackage from the information in the description file.


    
    gdal_translate -of GPKG file.xml file.gpkg -co TILE_FORMAT=JPEG
That was quite simple, right?
### The larger datasets way
If the command takes too much time, it means that it is trying to download too much data and could be caused by downloading higher resolution data than required.  
The command might even completely fail if it contains a request for bigger data blocks thant the server allows.
Here is the process to get larger datasets in a simple way. Let’s use a real example:
  1. Use `gdal_translate "WMS:https://www.gebco.net/data_and_products/gebco_web_services/web_map_service/mapserv?request=getmap&service=wms&crs=EPSG:4326&format=image/jpeg&layers=gebco_latest&version=1.1.0" test.xml -of WMS`
  2. Open the test.xml file for editing, here you’ll find the parameters of the WMS. We change the “SizeX” to 3600 and “SizeY” to 1800. By changing these parameters we lower the resolution. It is important to keep proportionality.
  3. Another thing we need to change are “BlockSizeX” and “BlockSizeY” that define the size of the tiles. We change both to 2048.
  4. Finally, use `gdal_translate -of GPKG test.xml test.gpkg -co TILE_FORMAT=JPEG`
  5. To make a Geopackage pyramid use `gdaladdo GPKG:test.gpkg:gebco_latest`. It will **replace** the Geopackage, if you want to keep the original one, you need to copy it first.


Now you have a raster Geopackage that you can use in QField.
## Testing raster formats
### Preparing the files
As first step we exported our test orthophoto WMS to a plain GeoTIFF using QGIS’ default behaviour.
![](../../../../../../i1.wp.com/www.opengis.ch/wp-content/uploads/2020/06/tiffc22d.png?fit=750%2C617&ssl=1)Default parameters used to create the initial tiff Format| gdal_translate| gdaladdo  
---|---|---  
gpkg JPEG| gdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_JPEG.gpkg” -co TILE_FORMAT=JPEG  |  | gpkg PNG| gdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_PNG.gpkg” -co TILE_FORMAT=PNG|  | gpkg PNG_JPEG| gdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_PNG_JPEG.gpkg” -co TILE_FORMAT=PNG_JPEG|   
gpkg PNG8| gdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_PNG8.gpkg” -co TILE_FORMAT=PNG8|   
gpkg WEBP| gdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_WEBP.gpkg” -co TILE_FORMAT=WEBP|   
gpkg pyramid_JPEG| gdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_JPEG.gpkg” -co TILE_FORMAT=JPEG| gdaladdo GPKG:C:\test\test_JPEG.gpkg:test_gpkg_JPEG   
gpkg pyramid_PNG| gdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_PNG.gpkg” -co TILE_FORMAT=PNG| gdaladdo GPKG:C:\test\test_PNG.gpkg:test_gpkg_PNG  
gpkg pyramid_PNG_JPEG| gdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_PNG_JPEG.gpkg” -co TILE_FORMAT=PNG_JPEG| gdaladdo GPKG:C:\test\test_PNG_JPEG.gpkg:test_gpkg_PNG_JPEG  
gpkg pyramid_PNG8| gdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_PNG8.gpkg” -co TILE_FORMAT=PNG8| gdaladdo GPKG:C:\test\test_PNG8.gpkg:test_gpkg_PNG8  
gpkg pyramid_WEBP| gdal_translate -of GPKG “C:\test\ortho_test.tif” “C:\test\test_WEBP.gpkg” -co TILE_FORMAT=WEBP| gdaladdo GPKG:C:\test\test_WEBP.gpkg:test_gpkg_WEBP  
JPEG2000| gdal_translate -of JP2OpenJPEG “C:\test\ortho_test.tif” “C:\test\test_jpeg_2000.jpg”|   
COG DEFLATE| gdal_translate “C:\test\ortho_test.tif” “C:\test\test_cog.tif” -co TILED=YES -co COPY_SRC_OVERVIEWS=YES -co COMPRESS=DEFLATE|   
COG_JPEG| gdal_translate “C:\test\ortho_test.tif” “C:\test\test_cog_JPEG.tif” -co TILED=YES -co COPY_SRC_OVERVIEWS=YES -co COMPRESS=JPEG|   
tif| In QGIS right click on the layer > export > save as > (see the details in the picture under the table)|   
MBT| gdal_translate -of MBTILES “C:\test\ortho_test.tif” “C:\test\test_mbt.mbtiles”|   
Creation commands for all the tested formats
### Rendering test results
We have tested many formats, here is a table with the results of the size and rendering speed in QGIS and QField.  
To analyze the speed we used `qgis_bench.exe -i 10 -p "C:\test\test.qgs" >> "C:\test\test.log`.  
Qgis_bench is a tool that renders a QGIS project a number of times to get performance measurements. The parameter -i is to define the iterations and -p is the project used which contains only the generated raster.
Format| Extent [m]| File size [GB]| Total_avg| Total_maxdev| Total_min| Total_stdev  
---|---|---|---|---|---|---  
gpkg JPEG| 52’880/29’230| 0.4| 250.242| 255.781| 5.539| 244.984  
gpkg PNG| 52’880/29’230| 2.9| 412.002| 490.328| 152.142| 259.859  
gpkg PNG_JPEG| 52’880/29’230| 0.4| 250.125| 256.875| 6.750| 245.172  
gpkg PNG8| 52’880/29’230| 1.4| 283.875| 296.406| 12.625| 271.250  
gpkg WEBP| 52’880/29’230| 0.3| 330.238| 348.109| 73.534| 256.703  
gpkg pyramid_JPEG| 52’880/29’230| 0.5| 1.009| 3.406| 2.397| 0.688  
gpkg pyramid_PNG| 52’880/29’230| 3.0| 1.208| 3.281| 2.073| 0.688  
gpkg pyramid_PNG_JPEG| 52’880/29’230| 0.6| 1.491| 4.344| 2.853| 1.016  
gpkg pyramid_PNG8| 52’880/29’230| 1.6| 1.508| 4.375| 2.867| 0.969  
gpkg pyramid_WEBP| 52’880/29’230| 0.4| 1.333| 4.906| 3.573| 0.766  
JPEG2000| 52’880/29’230| 1.1| 13.888| 136.109| 122.222| 0.219  
COG DEFLATE| 52’880/29’230| 3.6| 264.427| 273.094| 25.411| 239.016  
COG_JPEG| 52’880/29’230| 1.0| 14.778| 131.172| 116.394| 1.734  
tif| 52’880/29’230| 6.4| 2.367| 6.734| 4.367| 1.672  
MBT| 52’880/29’230| 4.4| 0.469| 4.641| 4.171| 0  
Comparison of file size and rendering speed of different raster formats. “Total” columns are rendering times in [s]. Lower file size is more storage friendly, lower Total_avg is more performant. 
## Analysis
### File size
The Geopackage WEBP (with and without pyramid) has the best result for file size, ~~but~~ it is ~~not _yet_ ~~supported by QField (from 1.6) and is ~~only~~ slightly smaller than the JPEG variant.
Plain GeoTiff, MBTiles, Cloud Optimized GeoTIFF (COG – DEFLATE mode) and Geopackages with PNG generate by far the largest file sizes (up to 20x larger) and are thus not recommended.
### Rendering speed
MBTiles are on average double as fast as JPEG Geopackages with pyramids which in turn are more than double as fast as GeoTIFF and 15x faster than COG.   
Geopackages without pyramids are 200 to 400 times slower.
## Conclusion
Even though MBTiles render faster than the Geopackage pyramid JPEG, they come with an almost 10x bigger storage requirement which makes us say that the best offline raster format supported by QField is **Geopackage pyramid JPEG** or if you need transparency and slightly smaller files **Geopackage pyramid WebP**.
If you need transparency before QField 1.6, the best results are achieved with Geopackage pyramid PNG_JPEG.
### _Related_
