import sys
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat

s1 = pd.read_csv(sys.argv[1], header = None)

s1c = s1.value_counts()

for j in sys.argv[4].split(','):

    bin = int(j)
    inc = 1
    l = int(sys.argv[2])
    r = int(sys.argv[3])
    seqLen = len(s1c[l:-(r)])

    idx, average = [],[]
    w = s1c.sort_index()
    for i in range(0, seqLen - bin, inc):
        idx.append(i + int(bin/2))
        average.append(stat.mean(w[l:-(r)][i:i+bin]))


    plt.figure(figsize=(12, 10), dpi=150)
    plt.plot(idx, average)
    plt.savefig(sys.argv[1][:-3] + str(bin) + '.png')