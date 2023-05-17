#!/bin/python

# Libraries
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

# Data set
df = pd.read_csv('FIG3-Aba/Aba_vir_merged_heatmap.csv')
df = df.set_index('Gene')

for i in range(df.shape[1]):
    for j in range(df.shape[0]):
        if df.iloc[j,i] == 0.0:
            df.iloc[j,i] = 97
#             print(j,i)
# df.tail()

# Create heatmap
sns.set(rc={'figure.figsize': (6, 10)})
# sns.heatmap(df, cmap = sns.cubehelix_palette(start=2, rot=0, dark=0, light=.95, as_cmap=True), linewidths = 0.50)
fig2 = sns.heatmap(df, cmap = sns.light_palette("seagreen", as_cmap=True), linewidths = 0.50, )
# sns.heatmap(df, cmap = sns.color_palette("Blues", as_cmap=True), linewidths = 0.50)

# Export heatmap
fig = fig2.get_figure()
fig.savefig('heatmap_Aba_vir.svg')  
