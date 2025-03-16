import pandas
import spei as si
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt

MM_PER_INCH = 25.4
START_YEAR = 1950

la_rainfall = pd.read_csv('../../source_data/la_rainfall.csv',)
source_data = pd.read_csv('../../source_data/la_rainfall.csv', index_col='Yr').iloc[1:-1]
source_data.drop('Annl', axis=1, inplace=True)
flattened_data = pd.Series()


for year, row in source_data[source_data.index > START_YEAR].iterrows():
    for key, val in row.items():
        val = val.replace('M', '')
        val = val.replace('T', '0')
        flattened_data[dt.strptime(f'{key} {year}', '%b %Y')] = float(val) * MM_PER_INCH


spi_df = pd.DataFrame(si.spi(flattened_data, timescale=3), columns=['spi3'])
print(spi_df)










