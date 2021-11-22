# rawplot.py
# INPUT: CSV file of 9 selected hexamer counts
# OUTPUT: Plot of raw and average reads of each count

import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat

bin = 15
shift = int((bin-1)/2)
inc = 1
seqLen = 1000


def plotCounts(ax, x, y, axestitle):
	average = []
	ax.set_title(axestitle, fontsize=20)
	ax.plot(x, y, color='0.5')
	for i in range(0, seqLen - bin, inc):
		average.append(stat.mean(y[i:i+bin]))
	ax.plot(x[shift+1:seqLen-shift], average, color='0')


rawCounts = pd.read_csv('hexamer_rawcounts_selected.csv')
pos = list(map(int, rawCounts.columns[1:]))
title = []
count = []
for index, row in rawCounts.iterrows():
	title.append(list(row)[0])
	count.append(list(row)[1:])

fig, ((ax0, ax1, ax2), (ax3, ax4, ax5), (ax6, ax7, ax8)) = plt.subplots(3, 3, sharex="all", sharey='row', figsize=(24, 16))

for i in range(9):
	plotCounts(eval("ax{}".format(i)), pos, count[i], title[i])

fig.suptitle("Frequency vs. Position from TSS", fontsize=30)
fig.supxlabel("Position from TSS", fontsize=30)
fig.supylabel("Frequency", fontsize=30)

plt.show()
