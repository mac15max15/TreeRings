import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from constants import *

data={}

def load_data(region):
    data[region] = pd.read_csv(f'../aggregated_data/{region}.csv')

def scale_weather(region):
    city = CITIES[region]

    city_temps = data[region][f'{city}_temp'].values.reshape(-1,1)
    data[region][f'{city}_scaled_temp'] = StandardScaler().fit_transform(city_temps)

    city_rainfall_lag1 = data[region][f'{city}_rainfall_lag1'].values.reshape(-1, 1)
    data[region][f'{city}_scaled_rainfall_lag1'] = StandardScaler().fit_transform(city_rainfall_lag1)

    city_rainfall = data[region][f'{city}_rainfall'].values.reshape(-1, 1)
    data[region][f'{city}_scaled_rainfall'] = StandardScaler().fit_transform(city_rainfall)


def main():
    for region in REGIONS:
        load_data(region)
        scale_weather(region)
        print(data[region])




if __name__ == '__main__':
    main()


