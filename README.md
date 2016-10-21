# playing-with-berlin-subways
This repository holds code used to analyze all the properties in Berlin, calculating their proximity (or lack thereof) to subway entrances.

For a quick look at code I used for a similar task in NYC, see this snippet:

https://github.com/patrickmaynard/playing-with-qgis-python/blob/master/test-eight.py

For a quick look at the source of my layer showing all Berlin properties, see this ESRI page:

http://opendata.esri-de.opendata.arcgis.com/datasets/d4ac5d6ff99140819d2033038664096c_0

For a quick look at how I got the second layer I needed (showing all subway entrances), see this Stack Exchange thread: 

http://gis.stackexchange.com/questions/214578/public-shp-file-showing-berlin-subway-entrances/

This task was inspired by I Quant NY:

http://iquantny.tumblr.com/post/99544282749/found-the-manhattan-apartment-thats-the-farthest

I copied tons of stuff from stack overflow, the QGIS docs and the python docs, including (but not necessarily limited to) the Haversine distance function, the csv writer, the layer-loading logic, etc.,. -- I just snapped it all together into something that functions pretty well for my purpose. 

# Making it work

To make this thing go, you'll need the two .shp files described above. Got them? Good.  

Now copy the code from here ...

https://github.com/patrickmaynard/playing-with-berlin-subways/blob/master/analyze.py 

... and paste it into your QGIS Python console. 

Then update the two lines that load .shp files, pointing them at the places where you saved those files.

Then update the location for the output csv file so that it points at your location of choice. 

Now set the argument in the final line (calling the Snobbery.importAndAnalyze() function) to something much higher than 5 -- a million is usually safe, since most cities do not have anywhere near a million properties.

Now hit the QGIS "run script" button and go take a nap. The script should eventually output a nice csv showing how far each property is from its nearest subway station. 

