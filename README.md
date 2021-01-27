# Energy Storage System Predictor

## Data Source
- 'ESS Data.xlsx' contains dataset for ESS installations. Obtained from https://www.sandia.gov/ess-ssl/global-energy-storage-database-home/ : Global Energy Storage Database Projects (11-17-2020). Accessed on Jan 18 2021.
- Data for elevation is obtained via Google Maps API. Refer to 'Get Elevation Data.py'
- Data for temperatures (contained in 'absolute.nc') is obtained from University of East Anglia Climatic Research Unit https://crudata.uea.ac.uk/cru/data/temperature/ : Absolute temperatures for the base period 1961-90 on a 5° by 5° grid (Jones et al., 1999). Refer to 'Temperature.py'

## Jupyter Notebook
- Implements machine learning model to predict type of energy storage system based on features of
  - Rated power in kW
  - Discharge duration in hours
  - Elevation of site
  - Elevation difference (i.e. topography) of site
  - Min, max and mean temperatures of site
