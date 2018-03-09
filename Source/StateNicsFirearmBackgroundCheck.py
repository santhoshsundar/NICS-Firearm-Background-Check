import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
sb.set()

df = pd.read_csv('../Data/nics-firearm-background-checks.csv')
df['year'] = [month.split('-')[0] for month in df['month'] ]

sorted_df = df.set_index(['year','month','state'])
sorted_df.sort_index(inplace=True)

year = sorted_df.index.levels[0].values
state = sorted_df.index.levels[2].values
year = year[1:]
year_tick = pd.np.arange(0, len(year))
state_tick = pd.np.arange(0,len(state))

state_sum = {}
for st in state:
    sum = []
    for yr in year:
        sum.append(sorted_df.loc[(yr),:,st]['totals'].sum())

    sum_series = pd.Series(sum,index=year)
    state_sum[st]=[sum_series.sum(),sum_series]

# # Individual state NICS Background Check Totals
# for key in state_sum.keys():
#     state_sum_series = state_sum[key][1]
#     ax = plt.subplot()
#     ax.figure.set_facecolor("#FFFFFF")
#     ax = state_sum_series.plot(kind="area", figsize=(12, 8), color="grey",alpha=0.75)
#     ax.set_title('Yearly ' + key + ' NICS Background Check Totals Since 1999', fontsize=22)
#     ax.set_xticks(year_tick)
#     ax.set_xticklabels(year)
#     ax.set_yticklabels([ "{0:,.0f}".format(y) for y in ax.get_yticks() ], fontsize=12)
#     plt.margins(x=0)
#     plt.savefig('../Charts/'+key+'_yearly.png')

# All states NICS Background Check Totals
state_sum_series = []
for key in state_sum.keys():
    state_sum_series.append(state_sum[key][0])

ind_state_sum = pd.Series(state_sum_series,index=state)
ax = plt.subplot()
ax.figure.set_facecolor("#FFFFFF")
ax = ind_state_sum.plot(kind="area", figsize=(12, 8), color="grey",alpha=0.75)
ax.set_title('State NICS Background Check Totals Since 1999', fontsize=22)
ax.set_xticks(state_tick)
ax.set_xticklabels(state)
ax.set_yticklabels([ "{0:,.0f}".format(y) for y in ax.get_yticks() ], fontsize=12)
sb.mpl.pyplot.setp(ax.get_xticklabels(), rotation=90, fontsize=12)
fig = plt.subplots_adjust(right=0.96,left=0.10,bottom=0.25)
plt.margins(x=0)
plt.savefig('../Charts/all_state_yearly.png')