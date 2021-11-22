# averageplot.py
# INPUT: CSV file of all possible hexamers
# OUTPUT: Plot of average counts of a chosen hexamer


import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat
import numpy as np

bin = 15
shift = int((bin-1)/2)
inc = 1
seqLen = 1000


def shadePlot(ax, x, y, axes_title):
	average = []
	ax.set_title(axes_title, fontsize=20)
	# ax.plot(x, y, color='0.5')
	for i in range(0, seqLen - bin, inc):
		average.append(stat.mean(y[i:i+bin]))
	average = np.array(average)
	ax.plot(x[shift+1:seqLen-shift], average, color='0', linewidth=2)
	baseline = stat.mean(y[:500])
	ax.axhline(y=baseline, xmin=0, xmax=1000, color='r', linestyle='--')
	ax.fill_between(x[shift+1:500], baseline, average[:492], color='0.4')
	ax.fill_between(x[500:seqLen-shift], baseline, average[492:], color='0.7', where=(average[492:]>baseline))


rawCounts = pd.read_csv('hexamer_rawcounts.csv')
pos = list(map(int, rawCounts.columns[1:]))
data = rawCounts.loc[rawCounts['Hexamer'] == 'CACGTG']
title = []
count = []
for index, row in data.iterrows():
	title.append(list(row)[0])
	count.append(list(row)[1:])
fig, ax = plt.subplots(1, 1, sharex="all", sharey='row', figsize=(15, 10))

shadePlot(ax, pos, count[0], title[0])
fig.suptitle("Frequency vs. Position from TSS (Peak Area)", fontsize=20)
fig.supxlabel("Position from TSS", fontsize=15)
fig.supylabel("Frequency", fontsize=15)
plt.show()
