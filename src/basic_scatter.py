import matplotlib.pyplot as plt
import matplotlib.patches as pat
import pandas as pd

from constants import *

DOT_SIZE = 0.05

socal_data = pd.read_csv(f'../aggregated_data/socal.csv')
sierra_data = pd.read_csv(f'../aggregated_data/sierra.csv')
colo_data = pd.read_csv('../aggregated_data/colo.csv')

c_socal, c_sierra, c_colo = pat.Circle((0, 0)), pat.Circle((0, 0)), pat.Circle((0, 0))
c_socal.set_color(SOCAL_COLOR)
c_sierra.set_color(SIERRA_COLOR)
c_colo.set_color(COLO_COLOR)

fig, ax = plt.subplots(squeeze=True)
ax.set_facecolor(BG_COLOR)
ax.scatter(socal_data['la_rainfall'], socal_data['avg_ring_width'], color=SOCAL_COLOR, linewidths=DOT_SIZE)
ax.scatter(sierra_data['bishop_rainfall'], sierra_data['avg_ring_width'], color=SIERRA_COLOR, linewidths=DOT_SIZE)
ax.scatter(colo_data['moab_rainfall'], colo_data['avg_ring_width'], color=COLO_COLOR, linewidths=DOT_SIZE)
ax.legend([c_socal, c_sierra, c_colo], [SOCAL_DISPLAY_NAME, SIERRA_DISPLAY_NAME, COLO_DISPLAY_NAME])
ax.set_xlabel('Annual Rainfall (in)')
ax.set_ylabel('Tree Ring Growth')

fig2, ax2 = plt.subplots(squeeze=True)
ax2.set_facecolor(BG_COLOR)
ax2.scatter(socal_data['la_temp'], socal_data['avg_ring_width'], color=SOCAL_COLOR, linewidths=DOT_SIZE)
ax2.scatter(sierra_data['bishop_temp'], sierra_data['avg_ring_width'], color=SIERRA_COLOR, linewidths=DOT_SIZE)
ax2.scatter(colo_data['moab_temp'], colo_data['avg_ring_width'], color=COLO_COLOR, linewidths=DOT_SIZE)
ax2.legend([c_socal, c_sierra, c_colo], [SOCAL_DISPLAY_NAME, SIERRA_DISPLAY_NAME, COLO_DISPLAY_NAME])
ax2.set_xlabel('Average Annual Temp (\u00B0F)')


plt.show()

