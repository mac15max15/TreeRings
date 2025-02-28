import pandas as pd
from sklearn.preprocessing import StandardScaler

from constants import *

'''
*******************************************************************************
This file takes in data from the tree ring dataset and raw historical weather data
and produces one output file for each region (la area, southern sierra, or upper
colorado river basin). Each output csv has the tree ring data for the sample locations
in that region, weather data for a city in the region, the average of the tree
ring growth over all the locations in that region, and a one year lag of recorded 
rainfall.

A lot of this could've been refactored into functions or to use variables defined
in constants.py, but since it only runs once and I'm lazy I haven't done it.
As far as I can tell it works, and the ugliness of this code allows the rest
of the code to be pretty.

-Max
********************************************************************************

'''


tree_data = pd.read_excel('../../source_data/SouthernCaliforniaChronologiesTable.xlsx')

# read the source data files and get the columns we need, then rename them to something intelligible
# also throw out the null values for weather stuff
bishop_rainfall = pd.read_csv('../../source_data/bishop_rainfall.csv')
bishop_rainfall = bishop_rainfall[bishop_rainfall['Annl'].notnull()]
bishop_rainfall = bishop_rainfall.loc[:, ['Yr', 'Annl']]
bishop_rainfall = bishop_rainfall.rename(columns={"Annl": "rainfall", 'Yr': 'Year'})

la_rainfall = pd.read_csv('../../source_data/la_rainfall.csv')
la_rainfall = la_rainfall[la_rainfall['Annl'].notnull()]
la_rainfall = la_rainfall.loc[:, ['Yr', 'Annl']]
la_rainfall = la_rainfall.rename(columns={"Annl": "rainfall", 'Yr': 'Year'})

moab_rainfall = pd.read_csv('../../source_data/moab_rainfall.csv')
moab_rainfall = moab_rainfall[moab_rainfall['Annl'].notnull()]
moab_rainfall = moab_rainfall.loc[:, ['Yr', 'Annl']]
moab_rainfall = moab_rainfall.rename(columns={"Annl": "rainfall", 'Yr': 'Year'})


bishop_temp = pd.read_csv('../../source_data/bishop_temp.csv', na_values='M')
bishop_temp = bishop_temp[bishop_temp['Annual'].notnull()]
bishop_temp = bishop_temp.loc[:, ['Year', 'Annual']]
bishop_temp = bishop_temp.rename(columns={"Annual": "temp"})

la_temp = pd.read_csv('../../source_data/la_temp.csv', na_values='M')
la_temp = la_temp[la_temp['Annual'].notnull()]
la_temp = la_temp.loc[:, ['Year', 'Annual']]
la_temp = la_temp.rename(columns={"Annual": "temp"})

moab_temp = pd.read_csv('../../source_data/moab_temp.csv', na_values='M')
moab_temp = moab_temp[moab_temp['Annual'].notnull()]
moab_temp = moab_temp.loc[:, ['Year', 'Annual']]
moab_temp = moab_temp.rename(columns={"Annual": "temp"})

# extract the tree data columns corresponding to locations in each region
southern_sierra_trees = tree_data.loc[:, ["Year", "PMN", "MWL", "MPS", "KSU", "LCU", "FCU", "PT9", "PT2", "LGU", "RRT", "HLC", "BIG", "LPK"]]
socal_trees = tree_data.loc[:, ["Year", "SBT", "GFS", "GFE", "GFN", "CTN", "CTS", "LCM"]]
colorado_river_trees = tree_data.loc[:, ["Year", "PUM", "RED", "TRG", "DOU", "WIL", "RCK", "DJU", "NPC"]]


# join it all up on year and calculate mean and lags.
sierra_agg_data = southern_sierra_trees.merge(bishop_rainfall, on='Year', how='inner')
sierra_agg_data = sierra_agg_data.merge(bishop_temp, on='Year', how='inner')
sierra_agg_data['avg_ring_width'] = sierra_agg_data[SIERRA_SITES].mean(axis=1)
sierra_agg_data['rainfall_lag1'] = sierra_agg_data['rainfall'].shift(1)

# remove the first row, which will have an na in the lag column, and the last row,
# which will have na bc this year's data isnt all in yet
sierra_agg_data = sierra_agg_data.iloc[1:-1]


socal_agg_data = socal_trees.merge(la_temp, on='Year', how='inner')
socal_agg_data = socal_agg_data.merge(la_rainfall, on='Year', how='inner')
socal_agg_data['rainfall_lag1'] = socal_agg_data['rainfall'].shift(1)
socal_agg_data['avg_ring_width'] = socal_agg_data[SOCAL_SITES].mean(axis=1)
socal_agg_data = socal_agg_data.iloc[1:-1]

colorado_agg_data = colorado_river_trees.merge(moab_temp, on='Year', how='inner')
colorado_agg_data = colorado_agg_data.merge(moab_rainfall, on='Year', how='inner')
colorado_agg_data['rainfall_lag1'] = colorado_agg_data['rainfall'].shift(1)
colorado_agg_data['avg_ring_width'] = colorado_agg_data[COLO_SITES].mean(axis=1)
colorado_agg_data = colorado_agg_data.iloc[1:-1]

data = {
    SOCAL: socal_agg_data,
    COLO: colorado_agg_data,
    SIERRA: sierra_agg_data
}

def preprocess_weather(region):
    city_temps = data[region]['temp'].values.reshape(-1,1)
    data[region]['scaled_temp'] = StandardScaler().fit_transform(city_temps)

    city_rainfall = data[region]['rainfall'].values.reshape(-1, 1)
    data[region]['scaled_rainfall'] = StandardScaler().fit_transform(city_rainfall)

    city_rainfall_lag1 = data[region]['rainfall_lag1'].values.reshape(-1, 1)
    data[region]['scaled_rainfall_lag1'] = StandardScaler().fit_transform(city_rainfall_lag1)


for region in REGIONS:
    preprocess_weather(region)
    data[region].to_csv(f'../../aggregated_data/{region}.csv')
