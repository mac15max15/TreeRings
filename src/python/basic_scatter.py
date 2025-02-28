import matplotlib.pyplot as plt
import matplotlib.patches as pat
import pandas as pd

from constants import *

DOT_SIZE = 0

socal_data = pd.read_csv('../../aggregated_data/socal.csv')
sierra_data = pd.read_csv('../../aggregated_data/sierra.csv')
colo_data = pd.read_csv('../../aggregated_data/colo.csv')

c_socal, c_sierra, c_colo = pat.Circle((0, 0)), pat.Circle((0, 0)), pat.Circle((0, 0))
c_socal.set_color(SOCAL_COLOR)
c_sierra.set_color(SIERRA_COLOR)
c_colo.set_color(COLO_COLOR)

fig, ax = plt.subplots(squeeze=True, figsize=(6, 8))
ax.set_facecolor(BG_COLOR)
ax.scatter(socal_data['scaled_rainfall'], socal_data['avg_ring_width'], color=SOCAL_COLOR, linewidths=DOT_SIZE)
ax.scatter(sierra_data['scaled_rainfall'], sierra_data['avg_ring_width'], color=SIERRA_COLOR, linewidths=DOT_SIZE)
ax.scatter(colo_data['scaled_rainfall'], colo_data['avg_ring_width'], color=COLO_COLOR, linewidths=DOT_SIZE)
ax.set_xlabel('Annual Rainfall (z-score)')
ax.set_ylabel('Tree Ring Growth')

fig2, ax2 = plt.subplots(squeeze=True, figsize=(6, 8))
ax2.set_facecolor(BG_COLOR)
ax2.scatter(socal_data['scaled_temp'], socal_data['avg_ring_width'], color=SOCAL_COLOR, linewidths=DOT_SIZE)
ax2.scatter(sierra_data['scaled_temp'], sierra_data['avg_ring_width'], color=SIERRA_COLOR, linewidths=DOT_SIZE)
ax2.scatter(colo_data['scaled_temp'], colo_data['avg_ring_width'], color=COLO_COLOR, linewidths=DOT_SIZE)
ax2.legend([c_socal, c_sierra, c_colo], REGION_DISPLAY_NAMES.values(), facecolor=LEGEND_BG_COLOR)
ax2.set_xlabel('Average Annual Temp (z-score)')


fig.savefig('../../graphics/precip_scatter.png', dpi=GRAPH_DPI)
fig2.savefig('../../graphics/temp_scatter.png', dpi=GRAPH_DPI)


