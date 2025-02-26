import pandas as pd
import numpy as np

tree_data = pd.read_excel('SouthernCaliforniaChronologiesTable.xlsx')

bishop_rainfall = pd.read_csv('bishop_rainfall.csv')
bishop_rainfall = bishop_rainfall[bishop_rainfall['Annl'].notnull()].loc[:, ['Yr', 'Annl']].rename(columns={"Annl": "bishpp_rainfall", 'Yr': 'Year'})

la_rainfall = pd.read_csv('la_rainfall.csv')
la_rainfall = la_rainfall[la_rainfall['Annl'].notnull()].loc[:, ['Yr', 'Annl']].rename(columns={"Annl": "la_rainfall", 'Yr': 'Year'})

moab_rainfall = pd.read_csv('moab_rainfall.csv')
moab_rainfall = moab_rainfall[moab_rainfall['Annl'].notnull()].loc[:, ['Yr', 'Annl']].rename(columns={"Annl": "moab_rainfall", 'Yr': 'Year'})

bishop_temp = pd.read_csv('bishop_temp.csv', na_values='M')
bishop_temp = bishop_temp[bishop_temp['Annual'].notnull()].loc[:, ['Year', 'Annual']].rename(columns={"Annual": "bishop_temp"})

la_temp = pd.read_csv('la_temp.csv', na_values='M')
la_temp = la_temp[la_temp['Annual'].notnull()].loc[:, ['Year', 'Annual']].rename(columns={"Annual": "la_temp"})

moab_temp = pd.read_csv('moab_temp.csv', na_values='M')
moab_temp = moab_temp[moab_temp['Annual'].notnull()].loc[:, ['Year', 'Annual']].rename(columns={"Annual": "moab_temp"})


southern_sierra_trees = tree_data.loc[:, ["Year", "PMN","MWL","MPS","KSU","LCU","FCU","PT9","PT2","LGU","RRT","HLC","BIG","LPK"]]
la_trees = tree_data.loc[:, ["Year","SBT","GFS","GFE","GFN","CTN","CTS","LCM"]]
colorado_river_trees = tree_data.loc[:, ["Year", "PUM","RED","TRG","DOU","WIL","RCK","DJU","NPC"]]

sierra_agg_data = southern_sierra_trees.join(bishop_temp.set_index('Year'), on='Year').join(bishop_rainfall.set_index('Year'), on='Year')
sierra_agg_data = sierra_agg_data[sierra_agg_data.notna().all(axis=1)]

la_agg_data = la_trees.join(la_temp.set_index('Year'), on='Year').join(la_rainfall.set_index('Year'), on='Year')
la_agg_data = la_agg_data[la_agg_data.notna().all(axis=1)]

colorado_agg_data = colorado_river_trees.join(moab_temp.set_index('Year'), on='Year').join(moab_rainfall.set_index('Year'), on='Year')
colorado_agg_data = colorado_agg_data[colorado_agg_data.notna().all(axis=1)]

la_agg_data.to_csv('aggregated_data/la.csv')
sierra_agg_data.to_csv('aggregated_data/sierra.csv')
colorado_agg_data.to_csv('aggregated_data/colorado_river.csv')





