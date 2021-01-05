import google.cloud
from google.cloud import bigquery
import geoplotlib
import os
import sys

if sys.version_info[0] < 3:
	raise EnvironmentError("Not runing Python 3")
else:
	print("Running Python " + str(sys.version_info[0]))
try:
	bigquery_client = bigquery.Client()
except EnvironmentError:
	print("You are not logged or have the wrong project selected use the command `gcloud auth login` to login to an account or `gcloud config set project PROJECT_ID` to set the project ID.")
	quit()

print("Connected to the bigquery client.")

bbox = geoplotlib.utils.BoundingBox(north=37.816091, west=-122.549661, south=37.69204, east=-122.335085)

query_job = bigquery_client.query('SELECT latitude AS lat, longitude AS lon, COUNT(*) FROM `bigquery-public-data.san_francisco.street_trees` GROUP BY lat, lon;')
assert query_job.state == 'RUNNING'

filename = 'trees.dat'
if not os.path.isfile(filename) or os.stat(filename).st_size < 5000 * 1000:
    with open(filename, 'w') as f:
        iterator = query_job.result(timeout=60)
        rows = list(iterator)
        f.write('lat,lon\n')
        for row in rows:
            if(row.lat and row.lon):
                f.write(str(row.lat) + ',' + str(row.lon) + '\n')

print("SF Tree data downloaded or read.")

data = geoplotlib.utils.read_csv(filename)
geoplotlib.hist(data, colorscale='sqrt', binsize=16, alpha=128)
geoplotlib.set_bbox(bbox)
print("Tree data ready to visualize")
geoplotlib.show()

