import pandas as pd
import numpy as np

'''
*******************************************************************************
This file takes in raw data from the tree ring dataset and historical weather data
and produces one output file for each region (la area, southern sierra, or upper
colorado river basin). Each output csv has the tree ring data for the sample locations
in that region, weather data for a city in the region, the average of the tree
ring growth over all the locations in that region, and a one year lag of recorded 
rainfall.

Note that the tree data is not 'raw' as the original authors of the study standardized
and 'detrended' the data. See the method section of the study linked in 'source_data/sourcs.txt' 
for more detail.

'''


tree_data = pd.read_excel('source_data/SouthernCaliforniaChronologiesTable.xlsx')

# read the source data files and get the columns we need, then rename them to something intelligible
bishop_rainfall = pd.read_csv('source_data/bishop_rainfall.csv')
bishop_rainfall = bishop_rainfall[bishop_rainfall['Annl'].notnull()]
bishop_rainfall = bishop_rainfall.loc[:, ['Yr', 'Annl']]
bishop_rainfall = bishop_rainfall.rename(columns={"Annl": "bishop_rainfall", 'Yr': 'Year'})

la_rainfall = pd.read_csv('source_data/la_rainfall.csv')
la_rainfall = la_rainfall[la_rainfall['Annl'].notnull()]
la_rainfall = la_rainfall.loc[:, ['Yr', 'Annl']]
la_rainfall = la_rainfall.rename(columns={"Annl": "la_rainfall", 'Yr': 'Year'})

moab_rainfall = pd.read_csv('source_data/moab_rainfall.csv')
moab_rainfall = moab_rainfall[moab_rainfall['Annl'].notnull()]
moab_rainfall = moab_rainfall.loc[:, ['Yr', 'Annl']]
moab_rainfall = moab_rainfall.rename(columns={"Annl": "moab_rainfall", 'Yr': 'Year'})


bishop_temp = pd.read_csv('source_data/bishop_temp.csv', na_values='M')
bishop_temp = bishop_temp[bishop_temp['Annual'].notnull()]
bishop_temp = bishop_temp.loc[:, ['Year', 'Annual']]
bishop_temp = bishop_temp.rename(columns={"Annual": "bishop_temp"})

la_temp = pd.read_csv('source_data/la_temp.csv', na_values='M')
la_temp = la_temp[la_temp['Annual'].notnull()]
la_temp = la_temp.loc[:, ['Year', 'Annual']]
la_temp = la_temp.rename(columns={"Annual": "la_temp"})

moab_temp = pd.read_csv('source_data/moab_temp.csv', na_values='M')
moab_temp = moab_temp[moab_temp['Annual'].notnull()]
moab_temp = moab_temp.loc[:, ['Year', 'Annual']]
moab_temp = moab_temp.rename(columns={"Annual": "moab_temp"})

# extract the tree data columns corresponding to locations in each region
southern_sierra_trees = tree_data.loc[:, ["Year", "PMN", "MWL", "MPS", "KSU", "LCU", "FCU", "PT9", "PT2", "LGU", "RRT", "HLC", "BIG", "LPK"]]
la_trees = tree_data.loc[:, ["Year", "SBT", "GFS", "GFE", "GFN", "CTN", "CTS", "LCM"]]
colorado_river_trees = tree_data.loc[:, ["Year", "PUM", "RED", "TRG", "DOU", "WIL", "RCK", "DJU", "NPC"]]


# join it all up on year
sierra_agg_data = southern_sierra_trees.join(bishop_temp.set_index('Year'), on='Year')
sierra_agg_data = sierra_agg_data.join(bishop_rainfall.set_index('Year'), on='Year')

# calculate mean and lag columns
sierra_agg_data['avg_ring_width'] = sierra_agg_data[[
    "PMN", "MWL", "MPS", "KSU", "LCU", "FCU", "PT9", "PT2", "LGU", "RRT", "HLC", "BIG", "LPK"
]].mean(axis=1)
sierra_agg_data['bishop_temp_lag1'] = sierra_agg_data['bishop_temp'].shift(1)

# filter out any row with an na value in it
sierra_agg_data = sierra_agg_data[sierra_agg_data.notna().all(axis=1)]

# Aggregate LA data
la_agg_data = la_trees.join(la_temp.set_index('Year'), on='Year')
la_agg_data = la_agg_data.join(la_rainfall.set_index('Year'), on='Year')
la_agg_data['la_temp_lag1'] = la_agg_data['la_temp'].shift(1)
la_agg_data = la_agg_data[la_agg_data.notna().all(axis=1)]

# Aggregate Colorado River data
colorado_agg_data = colorado_river_trees.join(moab_temp.set_index('Year'), on='Year')
colorado_agg_data = colorado_agg_data.join(moab_rainfall.set_index('Year'), on='Year')
colorado_agg_data['moab_temp_lag1'] = colorado_agg_data['moab_temp'].shift(1)
colorado_agg_data = colorado_agg_data[colorado_agg_data.notna().all(axis=1)]

# Save aggregated data to CSV files
la_agg_data.to_csv('aggregated_data/la.csv', index=False)
sierra_agg_data.to_csv('aggregated_data/sierra.csv', index=False)
colorado_agg_data.to_csv('aggregated_data/colorado_river.csv', index=False)
