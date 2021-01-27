from netCDF4 import Dataset
import pandas as pd
import math

climate_data = Dataset('absolute.nc')

# lats[0] = 87.5, lats[35] = -87.5
# lons[0] = -177.5, lons[71] = 177.5
# temp index with [month, lat, lon]
temps = climate_data['tem']

data = pd.read_csv('Data.csv')

data['Max Temp'] = 0
data['Min Temp'] = 0
data['Average Temp'] = 0

for i in range(len(data)):
    if math.isnan(data.iloc[i, data.columns.get_loc("Latitude")]) or math.isnan(data.iloc[i, data.columns.get_loc("Longitude")]):
        continue
    
    lat = -(data['Latitude'][i] - 87.5)/5.0
    lon = (data['Longitude'][i] + 177.5)/5.0
    data.iloc[i, data.columns.get_loc('Max Temp')] = temps[:, lat, lon].max()
    data.iloc[i, data.columns.get_loc('Min Temp')] = temps[:, lat, lon].min()
    data.iloc[i, data.columns.get_loc('Average Temp')] = temps[:, lat, lon].mean()
    
data.to_csv('Final Dataset.csv')

