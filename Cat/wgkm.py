import sys
import pandas as pd
import matplotlib.pyplot as plt

t3 = pd.read_csv(sys.argv[1], sep = '\t', header = None)

print('Shape:')
print(t3.shape)

t3[2] = t3[0].apply(lambda x: len(x))

tc = t3.groupby(2).count()
tm = t3.groupby(2).mean()
ts = t3.groupby(2).std()
tx = t3.groupby(2).max()
tu = t3.groupby(2).sum()


for k in t3[2].unique():
    t4 = t3[t3[2] == k]
    with open('kmfa/' + str(k) + '.fa', 'w') as f:
        for i, s in t4[0].iteritems():
            f.write('>' + str(i) + '\n')
            f.write(str(s) + '\n')


def pf(dt, s, e, suf):
    plt.figure(figsize=(12, 10), dpi=200)
    dt.loc[s:e,1].plot()
    plt.savefig(sys.argv[1] + suf)


#count upto 54
pf(tc, 0,50, '1_cnt_ex.png')

#focused count upto 54 
pf(tc, 11,50, '1_cnt_fc.png')

#mean upto 54
pf(tm, 0,50, '1_mean_ex.png')

#focused mean upto 54
pf(tm, 11,50, '1_mean_fc.png')

#std upto 54
pf(ts, 0,50, '1_std_ex.png')

#focused std upto 54
pf(ts, 11,50, '1_std_fc.png')

#max upto 54
pf(tx, 0,50, '1_max_ex.png')

#focused max upto 54
pf(tx, 11,50, '1_max_fc.png')

#sum upto 54
pf(tu, 0,50, '1_sum_ex.png')

#focused sum upto 54
pf(tu, 11,50, '1_sum_fc.png')
