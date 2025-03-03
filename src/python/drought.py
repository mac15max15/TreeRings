import pandas as pd
import numpy as np

la_rainfall = pd.read_csv('../../source_data/la_rainfall.csv')
print(la_rainfall['Annl'].mean())