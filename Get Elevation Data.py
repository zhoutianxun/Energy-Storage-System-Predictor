# To find the delta elevations of locations over approx 200m range 

import pandas as pd
import googlemaps
import math

data = pd.read_excel('ESS Data.xlsx')

data['Latitude_North'] = data['Latitude'] + 0.005
data['Latitude_South'] = data['Latitude'] - 0.005
data['Longitude_East'] = data['Longitude'] + 0.005
data['Longitude_West'] = data['Longitude'] - 0.005

data['Elevation'] = 0
data['Elevation_North'] = 0
data['Elevation_South'] = 0
data['Elevation_East'] = 0
data['Elevation_West'] = 0

# Replace key with valide Google client key
gmaps = googlemaps.Client(key='*****')

for i in range(len(data)):
    if math.isnan(data.iloc[i, data.columns.get_loc("Latitude")]) or math.isnan(data.iloc[i, data.columns.get_loc("Longitude")]):
        continue
    
    data.iloc[i, data.columns.get_loc("Elevation")] = gmaps.elevation((data['Latitude'][i], data['Longitude'][i]))[0]['elevation']
    data.iloc[i, data.columns.get_loc("Elevation_North")] = gmaps.elevation((data['Latitude_North'][i], data['Longitude'][i]))[0]['elevation']
    data.iloc[i, data.columns.get_loc("Elevation_South")] = gmaps.elevation((data['Latitude_South'][i], data['Longitude'][i]))[0]['elevation']
    data.iloc[i, data.columns.get_loc("Elevation_East")] = gmaps.elevation((data['Latitude'][i], data['Longitude_East'][i]))[0]['elevation']
    data.iloc[i, data.columns.get_loc("Elevation_West")] = gmaps.elevation((data['Latitude'][i], data['Longitude_West'][i]))[0]['elevation']
      
data.to_csv('Data.csv')