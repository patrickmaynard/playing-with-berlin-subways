import math
import csv

"""

This script analyzes subway entrances in Berlin. 

It outputs a csv file that allows us to rank each property in Berlin by its proximity (or lack thereof) to the closest subway station.

To analyse a useful number of properties, set the argument on the last line to something very high -- a million is usually safe.

All distances are as-the-crow-flies. 

Some logic is very obviously pulled straight from Python documentation. ("Spamwriter," for example.) No claim of originality is made here.

See README.md at https://github.com/patrickmaynard/playing-with-berlin-subways for more information on finding shapefiles, a few selective credits, inspiration, etc.,.



COMPLETED TODOs:
x Import logic from https://github.com/patrickmaynard/playing-with-qgis-python/blob/master/test-eight.py
x Update references to layer files so they don't reference NYC layers.
x Get rid of "centroid" reference, since both layers are points now -- actually, this does no harm. Leave it as-is.
x Fix fields that are printed.
x Fix labels on the csv file.
x Fix fields that are dumped to the csv file.
x Add UTF8 encoding for street names.
x Turn the csv-writing line back on.
x See if this thing works!

"""

class Snobbery(object):
    @staticmethod
    def haversine(lon1, lat1, lon2, lat2):
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a)) 
        km = 6367 * c
        return km

    @staticmethod
    def calculateDistance(featureProperty, layerEntrances):
        #This is a stub for what will eventually be our distance-to-closest-station function.
        shortestDistance = 1000
        featuresEntrances = layerEntrances.getFeatures()
        for featureEntrance in featuresEntrances:
                latEntrance = featureEntrance.geometry().centroid().asPoint().y()
                lonEntrance = featureEntrance.geometry().centroid().asPoint().x()
                latProperty = featureProperty.geometry().centroid().asPoint().y()
                lonProperty = featureProperty.geometry().centroid().asPoint().x()
                currentDistance = Snobbery.haversine(lonEntrance, latEntrance, lonProperty, latProperty)
                if currentDistance < shortestDistance:
                    shortestDistance = currentDistance
        return shortestDistance
        
    @staticmethod
    def importAndAnalyze(rowLimit = 3):
        layerProperties = iface.addVectorLayer("/Users/patrickmaynard/Downloads/Berlin_Hauskoordinaten_FServer_hosted/Berlin_Hauskoordinaten_FServer_hosted.shp", "Properties", "ogr")
        #^See the README file for details on how to get this shp file. (It was too large to include in my GitHub repository.)
        if not layerProperties:
          print "layerProperties failed to load!"
        layerEntrances = iface.addVectorLayer("/Users/patrickmaynard/Documents/GitHub/playing-with-berlin-subways/subway-entrances.shp", "Entrances", "ogr")
        #^See the README file for details on how to get an updated copy of this shp file. (I highly recommend getting the latest data.)
        if not layerEntrances:
          print "layerProperties failed to load!"
        features = layerProperties.getFeatures()
        counter = 0
        featuresSelected = []
        with open('/Users/patrickmaynard/Desktop/output.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            spamwriter.writerow(['STN','HNR', 'Lat','Lon', 'Distance'])
            for feature in features:
                if counter < rowLimit:
                    #print feature['hnr']
                    #print feature['stn']
                    #print Snobbery.calculateDistance(feature, layerEntrances)
                    print "Processed record " + str(counter) + " (out of about 375,339 records as of autumn 2016)."
                    try:
                        encodedStn = feature['stn'].encode('utf8')
                    except AttributeError:
                        encodedStn = "NULL"
                    spamwriter.writerow([encodedStn,feature['hnr'], feature.geometry().centroid().asPoint().y(),feature.geometry().centroid().asPoint().x(), Snobbery.calculateDistance(feature, layerEntrances)])

                counter += 1

        
Snobbery.importAndAnalyze(5)
