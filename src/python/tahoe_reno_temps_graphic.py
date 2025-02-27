import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


from constants import *


TAHOE_COLOR = 'dodgerblue'
RENO_COLOR = 'chocolate'

reno_data = pd.read_csv('../../source_data/reno_precip.csv')
reno_data = reno_data[reno_data['Yr']> 2013]
reno_data = reno_data[['Yr', 'Annl']]

tahoe_data = pd.read_csv('../../source_data/tahoe_city_precip.csv')
tahoe_data = tahoe_data[tahoe_data['Yr'] > 2013]
tahoe_data = tahoe_data[['Yr', 'Annl']]

aggregated_data = reno_data.merge(tahoe_data, on='Yr', suffixes=('_reno', '_tahoe'))
aggregated_data['ratio'] = aggregated_data['Annl_tahoe']/aggregated_data['Annl_reno']
aggregated_data['z_tahoe'] = StandardScaler().fit_transform(aggregated_data['Annl_tahoe'].values.reshape(-1,1))
aggregated_data['z_reno'] = StandardScaler().fit_transform(aggregated_data['Annl_reno'].values.reshape(-1,1))


fig, axs = plt.subplots(2,1, sharex=True, squeeze=True, layout='tight')

ax1 = axs[0]
aggregated_data.plot(
    x='Yr', y=['Annl_tahoe', 'Annl_reno'],
    style='o--',
    ax=ax1,
    color=[TAHOE_COLOR, RENO_COLOR]
)

ax1.set_ylabel('Precipitation (in)')

ax2 = axs[1]
aggregated_data.plot(
    x='Yr', y=['z_tahoe', 'z_reno'],
    style='o--',
    color=[TAHOE_COLOR, RENO_COLOR],
    ax=ax2
)

ax1.set_facecolor(BG_COLOR)
ax2.set_facecolor(BG_COLOR)

ax1.grid(True)
ax2.grid(True)

ax1.get_legend().remove()
ax2.get_legend().remove()


ax2.set_xlabel('Year')
ax2.set_ylabel('Precipitation (z-score)')
ax1.legend(['Tahoe', 'Reno'], loc='upper right')
fig.suptitle('Annual Precipitation for Lake Tahoe and Reno')

fig.savefig('../../graphics/renotahoe.png', dpi=GRAPH_DPI)



