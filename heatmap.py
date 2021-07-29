import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('files/speeding/Traffic_Crashes_-_Crashes.csv')

df2 = df[df['LATITUDE'] == 0]
df_loc = df[~df.index.isin(df2.index)]

# print(len(df3['LATITUDE']), len(df3['LONGITUDE']))
# df_dmg = df_loc[df_loc["DAMAGE"] != 'OVER $1,500']
# df_dmg1 = df[~df.index.isin(df_dmg.index)]
df_inj = df[df['MOST_SEVERE_INJURY'] == 'FATAL'] # maybe drop the over 1500 damages
df_inj = df_inj[df_inj['LOCATION'].notna()]
# print(len(df_inj))
counter = 0
for x in df_inj['INJURIES_TOTAL']:
    counter += x
counter2 = 0

same_name = {}
for x in df['STREET_NAME']:
    same_name[x] = same_name.get(x, 0)+1
sort_orders = sorted(same_name.items(), key=lambda x: x[1], reverse=True)
# print(sort_orders)
numbers = []
for x in sort_orders:
    if x[1] > 3000:
        numbers.append(x)

counter_injuries = 0
for x in numbers:
    counter_injuries += x[1]

# print(counter_injuries)

same_name_inj = {}
for x in df_inj['STREET_NAME']:
    same_name_inj[x] = same_name_inj.get(x, 0)+1
sort_orders1 = sorted(same_name_inj.items(), key=lambda x: x[1], reverse=True)
# print(sort_orders1)

# print(len(numbers))




# for x in sort_orders:
#     for y in x:
#      if y == type(int):
#        pass
#     else:
#         numbers.append(y)

# for x in numbers:
#     if x < 3000:
#         numbers.remove(x)

# print(numbers)

# incident_yr = {}
# for x in df_inj['CRASH_DATE']:
#     incident_yr[x[6:10]] = incident_yr.get(x[6:10],0) +1
#
# print(incident_yr)

# lighting_condition = {}
for x in df_inj['LIGHTING_CONDITION']:
    if x == 'DAYLIGHT':
        df_inj['LIGHTING_CONDITION'] = df_inj['LIGHTING_CONDITION'].replace({x: 1})

for x in df_inj['LIGHTING_CONDITION']:
    if x != 1:
        df_inj['LIGHTING_CONDITION'] = df_inj['LIGHTING_CONDITION'].replace({x: 0})

# print(df_inj['LIGHTING_CONDITION'])

for x in df_inj['WEATHER_CONDITION']:
    if x == 'CLEAR':
        df_inj['WEATHER_CONDITION'] = df_inj['WEATHER_CONDITION'].replace({x: 1})

for x in df_inj['WEATHER_CONDITION']:
    if x != 1:
        df_inj['WEATHER_CONDITION'] = df_inj['WEATHER_CONDITION'].replace({x: 0})

#       df_inj['WEATHER_CONDITION'] = df_inj['WEATHER_CONDITION'].replace({x: 0})

# print(df_inj['WEATHER_CONDITION'])

# print(df_inj[df_inj['WEATHER_CONDITION'] == 1])


# print(df_inj['LIGHTING_CONDITION'].unique())
months_list = []
for x in df_inj['CRASH_MONTH']:
    months = {'Months': x}
    months_list.append(months)
df_months = pd.DataFrame(months_list)
df_months.hist(bins=12, color='grey', edgecolor='black')

days_list = []
for x in df_inj['CRASH_DAY_OF_WEEK']:
    days = {'Day': x}
    days_list.append(days)
df_days = pd.DataFrame(days_list)
df_days.hist(bins=7, color='pink', edgecolor='black')

month_list = []
for x in df['CRASH_MONTH']:
    month = {'Months': x}
    month_list.append(month)
df_month = pd.DataFrame(month_list)
df_month.hist(bins=12, color='grey', edgecolor='black')

day_list = []
for x in df['CRASH_DAY_OF_WEEK']:
    days = {'Day': x}
    day_list.append(days)

df_day = pd.DataFrame(day_list)
df_day.hist(bins=7, color='pink', edgecolor='black')

# dict1 = {'water':firstFiveWaters()}
# data.append(dict1)


# print(day1)

# xx = pd.DataFrame({'Number of incidents': [63339, 72252, 74572, 73832, 74401, 84256, 77303]})

# xx.plot.hist()
df55 = df
for x in range(18, 24):
    df55["CRASH_HOUR"].replace({x: "evening"}, inplace=True)
for x in range(0, 5):
    df55["CRASH_HOUR"].replace({x: "night"}, inplace=True)
for x in range(5, 13):
    df55["CRASH_HOUR"].replace({x: "morning"}, inplace=True)
for x in range(12, 19):
    df55["CRASH_HOUR"].replace({x: "afternoon"}, inplace=True)
counter22 = 0

# for x in df55['CRASH_HOUR']:
#     if x == 'morning':
#         counter22+=1
# print(counter22)

df23 = pd.DataFrame({'time of day': ['Morning', 'Afternoon', 'Evening', 'Night'], ' morning(5,12)\n afternoon(13,18)\n evening(19,23)\n night(00, 04)': [173467, 186143, 120623, 39722]})
x334= df23.plot.bar(x='time of day', y=' morning(5,12)\n afternoon(13,18)\n evening(19,23)\n night(00, 04)', rot=0, color=['black', 'green', 'blue', 'red'])
x334.set_facecolor('yellow')
# incident_yr = {}
# for x in df_inj['CRASH_DATE']:
#     incident_yr[x[6:10]] = incident_yr.get(x[6:10],0) +1
#
# print(incident_yr)


for x in range(18, 24): #5
    df_inj["CRASH_HOUR"].replace({x: "evening"}, inplace=True)
for x in range(0, 5): # 4
    df_inj["CRASH_HOUR"].replace({x: "night"}, inplace=True)
for x in range(5, 13): # 7
    df_inj["CRASH_HOUR"].replace({x: "morning"}, inplace=True)
for x in range(12, 19): # 4
    df_inj["CRASH_HOUR"].replace({x: "afternoon"}, inplace=True)



# i_counter = 0
# for x in df['INTERSECTION_RELATED_I']:
#     if x == 'Y':
#         i_counter += 1
#
# #print(i_counter)


df_evening = df_inj[df_inj['CRASH_HOUR'] == 'evening']
df_night = df_inj[df_inj['CRASH_HOUR'] == 'night']
df_morning = df_inj[df_inj['CRASH_HOUR'] == 'morning']
df_afternoon = df_inj[df_inj['CRASH_HOUR'] == 'afternoon']
list12 = []

# df_time = pd.DataFrame({'lab':['M', 'Af', 'Ev'], 'count':[69,93, 127 ]})
# axxx = df.plot.bar(x='lab', y='count')

df14 = pd.DataFrame({'time of day': ['Morning', 'Afternoon', 'Evening', 'Night'], ' morning(5,12)\n afternoon(13,18)\n evening(19,23)\n night(00, 04)': [69, 93, 127, 137]})
axxxx = df14.plot.bar(x='time of day', y=' morning(5,12)\n afternoon(13,18)\n evening(19,23)\n night(00, 04)', rot=0, color=['black', 'green', 'blue', 'red'])
axxxx.set_facecolor("yellow")

chi_map = plt.imread("chigao_map.png")
fig, ax = plt.subplots(figsize=(18, 14))
ratio_size = (df_inj['LONGITUDE'].min(), df_inj['LONGITUDE'].max(), df_inj['LATITUDE'].min(), df_inj['LATITUDE'].max())
lat = df_inj[["LATITUDE"]]
long = df_inj[['LONGITUDE']]
ax.set_xlim(ratio_size[0], ratio_size[1])
ax.set_ylim(ratio_size[2], ratio_size[3])
# ax.scatter(df_morning.LONGITUDE, df_morning.LATITUDE, zorder=1, alpha=0.5, c='#03fce8', s=100)
# ax.scatter(df_afternoon.LONGITUDE, df_afternoon.LATITUDE, zorder=1, alpha=0.5, c='#235955', s=100)
# ax.scatter(df_evening.LONGITUDE, df_evening.LATITUDE, zorder=1, alpha=0.5, c='#ff5638', s=100)
# ax.scatter(df_night.LONGITUDE, df_night.LATITUDE, zorder=1, alpha=0.5, c='brown', s=100)

ax.scatter(df_morning.LONGITUDE, df_morning.LATITUDE, zorder=1, alpha=0.5, c='#03fce8', s=50)
ax.scatter(df_afternoon.LONGITUDE, df_afternoon.LATITUDE, zorder=1, alpha=0.5, c='#e34fbe', s=50)
ax.scatter(df_evening.LONGITUDE, df_evening.LATITUDE, zorder=1, alpha=0.5, c='#3c632c', s=50)
ax.scatter(df_night.LONGITUDE, df_night.LATITUDE, zorder=1, alpha=0.5, c='brown', s=50)
ax.legend(['MORNING', 'AFTERNOON', 'EVENING', 'NIGHT', ])
# print(len(df_evening), len(df_night), len(df_morning), len(df_afternoon) )
plt.imshow(chi_map, zorder=0, extent=ratio_size, aspect='equal')
plt.show()
