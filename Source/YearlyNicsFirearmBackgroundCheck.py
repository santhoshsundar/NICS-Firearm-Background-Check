import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
sb.set()

df = pd.read_csv('../Data/nics-firearm-background-checks.csv')
df['year'] = [month.split('-')[0] for month in df['month'] ]

totals_yearly = df.groupby('year')['totals'].sum()
totals_yearly = totals_yearly[1:]

tick = pd.np.arange(0, len(totals_yearly))

ax = plt.subplot()
ax.figure.set_facecolor("#FFFFFF")
ax = totals_yearly.plot(kind="area", figsize=(12, 8), color="grey",alpha=0.75)
ax.set_title("Yearly NICS Background Check Totals Since 1999", fontsize=24)
ax.set_xticks(tick)
ax.set_xticklabels([int(totals_yearly.index[i]) for i in range(len(totals_yearly))])
ax.set_yticklabels([ "{0:,.0f}".format(y) for y in ax.get_yticks() ], fontsize=12)
plt.margins(x=0)
plt.savefig('../Charts/year_nics_firearm_background_check.png')