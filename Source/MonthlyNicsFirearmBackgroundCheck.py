import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
sb.set()

df = pd.read_csv('../Data/nics-firearm-background-checks.csv')

totals_monthly = df.groupby('month')['totals'].sum()
totals_monthly = totals_monthly[2:]

ticks = pd.np.arange(2, len(totals_monthly), 12)

ax = plt.subplot()
ax.figure.set_facecolor("#FFFFFF")
ax = totals_monthly.plot(kind="area", figsize=(12, 8), color="grey", alpha=0.75)
ax.set_title("Monthly NICS Background Check Totals Since 1999", fontsize=24)
ax.set_xticks(ticks)
ax.set_xticklabels([ totals_monthly.index[i].split("-")[0] for i in ticks])
ax.set_yticklabels([ "{0:,.0f}".format(y) for y in ax.get_yticks() ], fontsize=12)
plt.margins(x=0)
plt.savefig('../Charts/month_nics_firearm_background_check.png')