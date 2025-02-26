import matplotlib.pyplot as plt
import pandas as pd

from constants import *

DOT_SIZE = 0.15

socal_data = pd.read_csv('../aggregated_data/socal.csv')
sierra_data = pd.read_csv('../aggregated_data/sierra.csv')
colo_data = pd.read_csv('../aggregated_data/colorado_river.csv')

fig, ax = plt.subplots(squeeze=True)
ax.scatter(socal_data['la_rainfall'], socal_data['avg_ring_width'], color=SOCAL_COLOR, linewidths=DOT_SIZE)
ax.scatter(sierra_data['bishop_rainfall'], sierra_data['avg_ring_width'], color=SIERRA_COLOR, linewidths=DOT_SIZE)
ax.scatter(colo_data['moab_rainfall'], colo_data['avg_ring_width'], color=COLO_COLOR, linewidths=DOT_SIZE)

ax.set_xlabel('Annual Rainfall (in)')
ax.set_ylabel('Tree Ring Growth')

fig2, ax2 = plt.subplots(squeeze=True)
ax.scatter(socal_data['la_rainfall'], socal_data['avg_ring_width'], color=SOCAL_COLOR, linewidths=DOT_SIZE)
ax.scatter(sierra_data['bishop_rainfall'], sierra_data['avg_ring_width'], color=SIERRA_COLOR, linewidths=DOT_SIZE)
ax.scatter(colo_data['moab_rainfall'], colo_data['avg_ring_width'], color=COLO_COLOR, linewidths=DOT_SIZE)

plt.show()

