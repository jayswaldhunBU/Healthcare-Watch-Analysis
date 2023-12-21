import pandas as pd
import matplotlib.pyplot as plt
dffridayam = pd.read_csv('FRIDAY AM2.csv')
dfdailyend=pd.read_csv("DAILY END2.csv")

dfavg=dfdailyend.groupby(['rsp_id']).mean() #finding the avg breaks for each rsp_id
df2breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]<=2]) #getting the rows with less than or equal to 2 avg breaks
df4breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]>=4]) #getting the rows with greater than or equal to 4 avg breaks

mergeddf2=pd.merge(dffridayam, df2breaks, on='rsp_id', how="right") #merge the dataframes
mergeddf4=pd.merge(dffridayam, df4breaks, on='rsp_id', how="right")

#calculate the florence scores (just adds all of them up)
mergeddf2["florence_score"]=mergeddf2["LIFE_SATISFACTION"]+mergeddf2["HAPPINESS"]+mergeddf2["PHYSICAL_HEALTH"]+mergeddf2["MENTAL_HEALTH"]+mergeddf2["WORTHWHILE"]+mergeddf2["PURPOSE"]+mergeddf2["PROMOTE_GOOD"]+mergeddf2["DELAYED_HAPPINESS"]+mergeddf2["CONTENT_RELATIONSHIPS"]+mergeddf2["SATISFYING_RELATIONSHIPS"]+mergeddf2["LIVING_EXPENSES"]+mergeddf2["FOOD_HOUSING"]
mergeddf4["florence_score"]=mergeddf4["LIFE_SATISFACTION"]+mergeddf4["HAPPINESS"]+mergeddf4["PHYSICAL_HEALTH"]+mergeddf4["MENTAL_HEALTH"]+mergeddf4["WORTHWHILE"]+mergeddf4["PURPOSE"]+mergeddf4["PROMOTE_GOOD"]+mergeddf4["DELAYED_HAPPINESS"]+mergeddf4["CONTENT_RELATIONSHIPS"]+mergeddf4["SATISFYING_RELATIONSHIPS"]+mergeddf4["LIVING_EXPENSES"]+mergeddf4["FOOD_HOUSING"]


#scatter plot
plt.scatter(mergeddf2['DAILY_BREAKS'], mergeddf2['florence_score'])
plt.scatter(mergeddf4['DAILY_BREAKS'], mergeddf4['florence_score'])
plt.xlabel("Average Daily Breaks") #x label
plt.ylabel("Florence Score") #y label
plt.title("2 Month Data")
plt.show()


dffridayam = pd.read_csv('FRIDAY AM3.csv')
dfdailyend=pd.read_csv("DAILY END3.csv")

dfavg=dfdailyend.groupby(['rsp_id']).mean() #finding the avg breaks for each rsp_id
df2breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]<=2]) #getting the rows with less than or equal to 2 avg breaks
df4breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]>=4]) #getting the rows with greater than or equal to 4 avg breaks

mergeddf2=pd.merge(dffridayam, df2breaks, on='rsp_id', how="right") #merge the dataframes
mergeddf4=pd.merge(dffridayam, df4breaks, on='rsp_id', how="right")

#calculate the florence scores (just adds all of them up)
mergeddf2["florence_score"]=mergeddf2["LIFE_SATISFACTION"]+mergeddf2["HAPPINESS"]+mergeddf2["PHYSICAL_HEALTH"]+mergeddf2["MENTAL_HEALTH"]+mergeddf2["WORTHWHILE"]+mergeddf2["PURPOSE"]+mergeddf2["PROMOTE_GOOD"]+mergeddf2["DELAYED_HAPPINESS"]+mergeddf2["CONTENT_RELATIONSHIPS"]+mergeddf2["SATISFYING_RELATIONSHIPS"]+mergeddf2["LIVING_EXPENSES"]+mergeddf2["FOOD_HOUSING"]
mergeddf4["florence_score"]=mergeddf4["LIFE_SATISFACTION"]+mergeddf4["HAPPINESS"]+mergeddf4["PHYSICAL_HEALTH"]+mergeddf4["MENTAL_HEALTH"]+mergeddf4["WORTHWHILE"]+mergeddf4["PURPOSE"]+mergeddf4["PROMOTE_GOOD"]+mergeddf4["DELAYED_HAPPINESS"]+mergeddf4["CONTENT_RELATIONSHIPS"]+mergeddf4["SATISFYING_RELATIONSHIPS"]+mergeddf4["LIVING_EXPENSES"]+mergeddf4["FOOD_HOUSING"]


#scatter plot
plt.scatter(mergeddf2['DAILY_BREAKS'], mergeddf2['florence_score'])
plt.scatter(mergeddf4['DAILY_BREAKS'], mergeddf4['florence_score'])
plt.xlabel("Average Daily Breaks") #x label
plt.ylabel("Florence Score") #y label
plt.title("3 Month Data")
plt.show()


dffridayam = pd.read_csv('FRIDAY AM4.csv')
dfdailyend=pd.read_csv("DAILY END4.csv")

dfavg=dfdailyend.groupby(['rsp_id']).mean() #finding the avg breaks for each rsp_id
df2breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]<=2]) #getting the rows with less than or equal to 2 avg breaks
df4breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]>=4]) #getting the rows with greater than or equal to 4 avg breaks

mergeddf2=pd.merge(dffridayam, df2breaks, on='rsp_id', how="right") #merge the dataframes
mergeddf4=pd.merge(dffridayam, df4breaks, on='rsp_id', how="right")

#calculate the florence scores (just adds all of them up)
mergeddf2["florence_score"]=mergeddf2["LIFE_SATISFACTION"]+mergeddf2["HAPPINESS"]+mergeddf2["PHYSICAL_HEALTH"]+mergeddf2["MENTAL_HEALTH"]+mergeddf2["WORTHWHILE"]+mergeddf2["PURPOSE"]+mergeddf2["PROMOTE_GOOD"]+mergeddf2["DELAYED_HAPPINESS"]+mergeddf2["CONTENT_RELATIONSHIPS"]+mergeddf2["SATISFYING_RELATIONSHIPS"]+mergeddf2["LIVING_EXPENSES"]+mergeddf2["FOOD_HOUSING"]
mergeddf4["florence_score"]=mergeddf4["LIFE_SATISFACTION"]+mergeddf4["HAPPINESS"]+mergeddf4["PHYSICAL_HEALTH"]+mergeddf4["MENTAL_HEALTH"]+mergeddf4["WORTHWHILE"]+mergeddf4["PURPOSE"]+mergeddf4["PROMOTE_GOOD"]+mergeddf4["DELAYED_HAPPINESS"]+mergeddf4["CONTENT_RELATIONSHIPS"]+mergeddf4["SATISFYING_RELATIONSHIPS"]+mergeddf4["LIVING_EXPENSES"]+mergeddf4["FOOD_HOUSING"]


#scatter plot
plt.scatter(mergeddf2['DAILY_BREAKS'], mergeddf2['florence_score'])
plt.scatter(mergeddf4['DAILY_BREAKS'], mergeddf4['florence_score'])
plt.xlabel("Average Daily Breaks") #x label
plt.ylabel("Florence Score") #y label
plt.title("4 Month Data")
plt.show()