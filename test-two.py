#Here I am just testing the ability to load a couple layers.
#Modified from http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadlayer.html

#For test one, see https://github.com/patrickmaynard/playing-with-qgis-python/blob/master/test-one

layerProperties = iface.addVectorLayer("/Users/patrickmaynard/Downloads/Berlin_Hauskoordinaten_FServer_hosted/Berlin_Hauskoordinaten_FServer_hosted.shp", "Properties", "ogr")
if not layerProperties:
  print "layerProperties failed to load!"
  
layerEntrances = iface.addVectorLayer("/Users/patrickmaynard/Documents/GitHub/playing-with-berlin-subways/subway-entrances.shp", "Entrances", "ogr")
if not layerEntrances:
    print "layerEntrances failed to load!"
