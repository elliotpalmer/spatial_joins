import pandas as pd
import geopandas as gpd

zip_url = 'https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON/master/oh_ohio_zip_codes_geo.min.json'

# Return the data
print('Getting Zip Code Shapefile Data...')
response = requests.get(zip_url)
zips = response.json()

jobs = pd.read_csv('./data/jobs.csv')