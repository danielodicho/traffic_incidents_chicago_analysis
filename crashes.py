import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('files/speeding/Traffic_Crashes_-_Crashes.csv')
df55 = df
for x in range(18, 24):
    df55["CRASH_HOUR"].replace({x: "evening"}, inplace=True)
for x in range(0, 5):
    df55["CRASH_HOUR"].replace({x: "night"}, inplace=True)
for x in range(5, 13):
    df55["CRASH_HOUR"].replace({x: "morning"}, inplace=True)
for x in range(12, 19):
    df55["CRASH_HOUR"].replace({x: "afternoon"}, inplace=True)
df_inj = df[df['MOST_SEVERE_INJURY'] == 'FATAL']
df_inj = df_inj[df_inj['DAMAGE'] == 'OVER $1,500']
df2 = df_inj[['CRASH_DAY_OF_WEEK', 'CRASH_HOUR']]

df_monday = df2[df2['CRASH_DAY_OF_WEEK'] == 1]
counter22 = 0
for x in df55['CRASH_HOUR']:
    if x == 'evening':
        counter22+=1
print(counter22)
# morning = , afternoon = 10, evening = 19 , night =
df23 = pd.DataFrame({'Time of incident, Mondays': ['Morning', 'Afternoon', 'Evening', 'Night'], ' morning(5,12)\n afternoon(13,18)\n evening(19,23)\n night(00, 04)': [15, 10, 19, 41]})
x334= df23.plot.bar(x='Time of incident, Mondays', y=' morning(5,12)\n afternoon(13,18)\n evening(19,23)\n night(00, 04)', rot=0, color=['black', 'green', 'blue', 'red'])
# plt.show()