# AQS API Config Defaults
# API Reference: https://aqs.epa.gov/aqsweb/documents/data_api.htmls

# API Connection:
apiURL = 'https://aqs.epa.gov/data/api/sampleData/byBox?'
apiUser = 'ronneimark@hotmail.com'
apiPassword = 'tawnybird31'


# Sample constructed url: 
# Example returns ozone annual summaries in the vicinity of central Alabama for the first two days in May, 2015:
# https://aqs.epa.gov/data/api/annualData/byBox?email=test@aqs.api&key=test&param=44201&bdate=20150501&edate=20150502&minlat=33.3&maxlat=33.6&minlon=-87.0&maxlon=-86.7
# Query Parameters:

aqsParams = {'Carbon Monoxide': '42101',
            'Sulfur Dioxide': '42401',
             'Nitrogen Oxide': '42602',
             'Ozone': '44201',
             'PMI 2.5': '88101'}

# USGS API Config Defaults
# API Reference: 
usgsURL = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
usgsFormat = 'format=geojson'
usgsStart = '&starttime=1990-01-01'
usgsMinmag = '&minmagnitude=5.0'
## Lat/Long Bounding box for the CONUS
usgsConus = {'minlat': '&minlatitude=24.7433195', 
            'maxlat': '&maxlatitude=49.3457868',
            'minlon': '&minlongitude=-124.7844079',
            'maxlon': '&maxlongitude=-66.9513812'}
# Target Parameters