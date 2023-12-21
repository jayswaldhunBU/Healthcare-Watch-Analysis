import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.stats import kendalltau, pearsonr, spearmanr
def pearsonr_pval(x,y):
        return pearsonr(x,y)[1]

dffridayam = pd.read_csv('FRIDAY AM6.csv')
dfdailyend=pd.read_csv("DAILY END6.csv")

dffridayam['local_time'] = pd.to_datetime(dffridayam['local_time']) #get only the data from within this timeframe (removing the data from all the previous months)
dfdailyend['local_time'] = pd.to_datetime(dfdailyend['local_time']) 
start_date=datetime(2022, 5, 1, 0, 0, 0, 0)
end_date=datetime(2022, 8, 1, 0, 0, 0, 0)
dffridayam=pd.DataFrame(dffridayam.loc[(dffridayam['local_time'] > start_date) & (dffridayam['local_time'] < end_date)])
dfdailyend=pd.DataFrame(dfdailyend.loc[(dfdailyend['local_time'] > start_date) & (dfdailyend['local_time'] < end_date)])

dfavg=dfdailyend.groupby(['rsp_id']).mean() #finding the avg breaks for each rsp_id
df2breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]<=2]) #getting the rows with less than or equal to 2 avg breaks
df4breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]>=4]) #getting the rows with greater than or equal to 4 avg breaks

mergeddf2=pd.merge(dffridayam, df2breaks, on='rsp_id', how="right") #merge the dataframes
mergeddf4=pd.merge(dffridayam, df4breaks, on='rsp_id', how="right")

#calculate the florence scores (just adds all of them up)
mergeddf2["flourishing_score"]=mergeddf2["LIFE_SATISFACTION"]+mergeddf2["HAPPINESS"]+mergeddf2["PHYSICAL_HEALTH"]+mergeddf2["MENTAL_HEALTH"]+mergeddf2["WORTHWHILE"]+mergeddf2["PURPOSE"]+mergeddf2["PROMOTE_GOOD"]+mergeddf2["DELAYED_HAPPINESS"]+mergeddf2["CONTENT_RELATIONSHIPS"]+mergeddf2["SATISFYING_RELATIONSHIPS"]+mergeddf2["LIVING_EXPENSES"]+mergeddf2["FOOD_HOUSING"]
mergeddf4["flourishing_score"]=mergeddf4["LIFE_SATISFACTION"]+mergeddf4["HAPPINESS"]+mergeddf4["PHYSICAL_HEALTH"]+mergeddf4["MENTAL_HEALTH"]+mergeddf4["WORTHWHILE"]+mergeddf4["PURPOSE"]+mergeddf4["PROMOTE_GOOD"]+mergeddf4["DELAYED_HAPPINESS"]+mergeddf4["CONTENT_RELATIONSHIPS"]+mergeddf4["SATISFYING_RELATIONSHIPS"]+mergeddf4["LIVING_EXPENSES"]+mergeddf4["FOOD_HOUSING"]


#scatter plot
plt.scatter(mergeddf2['DAILY_BREAKS'], mergeddf2['flourishing_score'])
plt.scatter(mergeddf4['DAILY_BREAKS'], mergeddf4['flourishing_score'])
plt.xlabel("Average Daily Breaks") #x label
plt.ylabel("Flourishing Score") #y label
plt.title("2 Month Data")
plt.show()
print("Mean Flourishing Score of 2 or Less Breaks (2 Month)= "+str(mergeddf2['flourishing_score'].mean()))
print("Mean Flourishing Score of 4 or More Breaks (2 Month)= "+str(mergeddf4['flourishing_score'].mean()))

############################################

dffridayam = pd.read_csv('FRIDAY AM6.csv')
dfdailyend=pd.read_csv("DAILY END6.csv")

dffridayam['local_time'] = pd.to_datetime(dffridayam['local_time']) #get only the data from within this timeframe (removing the data from all the previous months)
dfdailyend['local_time'] = pd.to_datetime(dfdailyend['local_time']) 
start_date=datetime(2022, 8, 1, 0, 0, 0, 0)
end_date=datetime(2022, 9, 1, 0, 0, 0, 0)
dffridayam=pd.DataFrame(dffridayam.loc[(dffridayam['local_time'] > start_date) & (dffridayam['local_time'] < end_date)])
dfdailyend=pd.DataFrame(dfdailyend.loc[(dfdailyend['local_time'] > start_date) & (dfdailyend['local_time'] < end_date)])

dfavg=dfdailyend.groupby(['rsp_id']).mean() #finding the avg breaks for each rsp_id
df2breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]<=2]) #getting the rows with less than or equal to 2 avg breaks
df4breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]>=4]) #getting the rows with greater than or equal to 4 avg breaks

mergeddf2=pd.merge(dffridayam, df2breaks, on='rsp_id', how="right") #merge the dataframes
mergeddf4=pd.merge(dffridayam, df4breaks, on='rsp_id', how="right")

#calculate the florence scores (just adds all of them up)
mergeddf2["flourishing_score"]=mergeddf2["LIFE_SATISFACTION"]+mergeddf2["HAPPINESS"]+mergeddf2["PHYSICAL_HEALTH"]+mergeddf2["MENTAL_HEALTH"]+mergeddf2["WORTHWHILE"]+mergeddf2["PURPOSE"]+mergeddf2["PROMOTE_GOOD"]+mergeddf2["DELAYED_HAPPINESS"]+mergeddf2["CONTENT_RELATIONSHIPS"]+mergeddf2["SATISFYING_RELATIONSHIPS"]+mergeddf2["LIVING_EXPENSES"]+mergeddf2["FOOD_HOUSING"]
mergeddf4["flourishing_score"]=mergeddf4["LIFE_SATISFACTION"]+mergeddf4["HAPPINESS"]+mergeddf4["PHYSICAL_HEALTH"]+mergeddf4["MENTAL_HEALTH"]+mergeddf4["WORTHWHILE"]+mergeddf4["PURPOSE"]+mergeddf4["PROMOTE_GOOD"]+mergeddf4["DELAYED_HAPPINESS"]+mergeddf4["CONTENT_RELATIONSHIPS"]+mergeddf4["SATISFYING_RELATIONSHIPS"]+mergeddf4["LIVING_EXPENSES"]+mergeddf4["FOOD_HOUSING"]


#scatter plot
plt.scatter(mergeddf2['DAILY_BREAKS'], mergeddf2['flourishing_score'])
plt.scatter(mergeddf4['DAILY_BREAKS'], mergeddf4['flourishing_score'])
plt.xlabel("Average Daily Breaks") #x label
plt.ylabel("Flourishing Score") #y label
plt.title("3 Month Data")
plt.show()
print("Mean Flourishing Score of 2 or Less Breaks (3 Month)= "+str(mergeddf2['flourishing_score'].mean()))
print("Mean Flourishing Score of 4 or More Breaks (3 Month)= "+str(mergeddf4['flourishing_score'].mean()))

############################################

dffridayam = pd.read_csv('FRIDAY AM6.csv')
dfdailyend=pd.read_csv("DAILY END6.csv")

dffridayam['local_time'] = pd.to_datetime(dffridayam['local_time']) #get only the data from within this timeframe (removing the data from all the previous months)
dfdailyend['local_time'] = pd.to_datetime(dfdailyend['local_time']) 
start_date=datetime(2022, 9, 1, 0, 0, 0, 0)
end_date=datetime(2022, 10, 1, 0, 0, 0, 0)
dffridayam=pd.DataFrame(dffridayam.loc[(dffridayam['local_time'] > start_date) & (dffridayam['local_time'] < end_date)])
dfdailyend=pd.DataFrame(dfdailyend.loc[(dfdailyend['local_time'] > start_date) & (dfdailyend['local_time'] < end_date)])

dfavg=dfdailyend.groupby(['rsp_id']).mean() #finding the avg breaks for each rsp_id
df2breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]<=2]) #getting the rows with less than or equal to 2 avg breaks
df4breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]>=4]) #getting the rows with greater than or equal to 4 avg breaks

mergeddf2=pd.merge(dffridayam, df2breaks, on='rsp_id', how="right") #merge the dataframes
mergeddf4=pd.merge(dffridayam, df4breaks, on='rsp_id', how="right")

#calculate the florence scores (just adds all of them up)
mergeddf2["flourishing_score"]=mergeddf2["LIFE_SATISFACTION"]+mergeddf2["HAPPINESS"]+mergeddf2["PHYSICAL_HEALTH"]+mergeddf2["MENTAL_HEALTH"]+mergeddf2["WORTHWHILE"]+mergeddf2["PURPOSE"]+mergeddf2["PROMOTE_GOOD"]+mergeddf2["DELAYED_HAPPINESS"]+mergeddf2["CONTENT_RELATIONSHIPS"]+mergeddf2["SATISFYING_RELATIONSHIPS"]+mergeddf2["LIVING_EXPENSES"]+mergeddf2["FOOD_HOUSING"]
mergeddf4["flourishing_score"]=mergeddf4["LIFE_SATISFACTION"]+mergeddf4["HAPPINESS"]+mergeddf4["PHYSICAL_HEALTH"]+mergeddf4["MENTAL_HEALTH"]+mergeddf4["WORTHWHILE"]+mergeddf4["PURPOSE"]+mergeddf4["PROMOTE_GOOD"]+mergeddf4["DELAYED_HAPPINESS"]+mergeddf4["CONTENT_RELATIONSHIPS"]+mergeddf4["SATISFYING_RELATIONSHIPS"]+mergeddf4["LIVING_EXPENSES"]+mergeddf4["FOOD_HOUSING"]

#scatter plot
plt.scatter(mergeddf2['DAILY_BREAKS'], mergeddf2['flourishing_score'])
plt.scatter(mergeddf4['DAILY_BREAKS'], mergeddf4['flourishing_score'])
plt.xlabel("Average Daily Breaks") #x label
plt.ylabel("Flourishing Score") #y label
plt.title("4 Month Data")
plt.show()
print("Mean Flourishing Score of 2 or Less Breaks (4 Month)= "+str(mergeddf2['flourishing_score'].mean()))
print("Mean Flourishing Score of 4 or More Breaks (4 Month)= "+str(mergeddf4['flourishing_score'].mean()))

############################################

dffridayam = pd.read_csv('FRIDAY AM6.csv')
dfdailyend=pd.read_csv("DAILY END6.csv")

dffridayam['local_time'] = pd.to_datetime(dffridayam['local_time']) #get only the data from within this timeframe (removing the data from all the previous months)
dfdailyend['local_time'] = pd.to_datetime(dfdailyend['local_time']) 
start_date=datetime(2022, 10, 1, 0, 0, 0, 0)
end_date=datetime(2022, 12, 1, 0, 0, 0, 0)
dffridayam=pd.DataFrame(dffridayam.loc[(dffridayam['local_time'] > start_date) & (dffridayam['local_time'] < end_date)])
dfdailyend=pd.DataFrame(dfdailyend.loc[(dfdailyend['local_time'] > start_date) & (dfdailyend['local_time'] < end_date)])

dfavg=dfdailyend.groupby(['rsp_id']).mean() #finding the avg breaks for each rsp_id
df2breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]<=2]) #getting the rows with less than or equal to 2 avg breaks
df4breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]>=4]) #getting the rows with greater than or equal to 4 avg breaks

mergeddf2=pd.merge(dffridayam, df2breaks, on='rsp_id', how="right") #merge the dataframes
mergeddf4=pd.merge(dffridayam, df4breaks, on='rsp_id', how="right")

#calculate the florence scores (just adds all of them up)
mergeddf2["flourishing_score"]=mergeddf2["LIFE_SATISFACTION"]+mergeddf2["HAPPINESS"]+mergeddf2["PHYSICAL_HEALTH"]+mergeddf2["MENTAL_HEALTH"]+mergeddf2["WORTHWHILE"]+mergeddf2["PURPOSE"]+mergeddf2["PROMOTE_GOOD"]+mergeddf2["DELAYED_HAPPINESS"]+mergeddf2["CONTENT_RELATIONSHIPS"]+mergeddf2["SATISFYING_RELATIONSHIPS"]+mergeddf2["LIVING_EXPENSES"]+mergeddf2["FOOD_HOUSING"]
mergeddf4["flourishing_score"]=mergeddf4["LIFE_SATISFACTION"]+mergeddf4["HAPPINESS"]+mergeddf4["PHYSICAL_HEALTH"]+mergeddf4["MENTAL_HEALTH"]+mergeddf4["WORTHWHILE"]+mergeddf4["PURPOSE"]+mergeddf4["PROMOTE_GOOD"]+mergeddf4["DELAYED_HAPPINESS"]+mergeddf4["CONTENT_RELATIONSHIPS"]+mergeddf4["SATISFYING_RELATIONSHIPS"]+mergeddf4["LIVING_EXPENSES"]+mergeddf4["FOOD_HOUSING"]


#scatter plot
plt.scatter(mergeddf2['DAILY_BREAKS'], mergeddf2['flourishing_score'])
plt.scatter(mergeddf4['DAILY_BREAKS'], mergeddf4['flourishing_score'])
plt.xlabel("Average Daily Breaks") #x label
plt.ylabel("Flourishing Score") #y label
plt.title("6 Month Data")
plt.show()
print("Mean Flourishing Score of 2 or Less Breaks (6 Month)= "+str(mergeddf2['flourishing_score'].mean()))
print("Mean Flourishing Score of 4 or More Breaks (6 Month)= "+str(mergeddf4['flourishing_score'].mean()))
    
#####################################
dffridayam = pd.read_csv('FRIDAY AM6.csv')
dfdailyend=pd.read_csv("DAILY END6.csv")

dfavg=dfdailyend.groupby(['rsp_id']).mean() #finding the avg breaks for each rsp_id
df2breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]<=2]) #getting the rows with less than or equal to 2 avg breaks
df4breaks=pd.DataFrame(dfavg.loc[dfavg["DAILY_BREAKS"]>=4]) #getting the rows with greater than or equal to 4 avg breaks

mergeddf2=pd.merge(dffridayam, df2breaks, on='rsp_id', how="right") #merge the dataframes
mergeddf4=pd.merge(dffridayam, df4breaks, on='rsp_id', how="right")

#calculate the florence scores (just adds all of them up)
mergeddf2["flourishing_score"]=mergeddf2["LIFE_SATISFACTION"]+mergeddf2["HAPPINESS"]+mergeddf2["PHYSICAL_HEALTH"]+mergeddf2["MENTAL_HEALTH"]+mergeddf2["WORTHWHILE"]+mergeddf2["PURPOSE"]+mergeddf2["PROMOTE_GOOD"]+mergeddf2["DELAYED_HAPPINESS"]+mergeddf2["CONTENT_RELATIONSHIPS"]+mergeddf2["SATISFYING_RELATIONSHIPS"]+mergeddf2["LIVING_EXPENSES"]+mergeddf2["FOOD_HOUSING"]
mergeddf4["flourishing_score"]=mergeddf4["LIFE_SATISFACTION"]+mergeddf4["HAPPINESS"]+mergeddf4["PHYSICAL_HEALTH"]+mergeddf4["MENTAL_HEALTH"]+mergeddf4["WORTHWHILE"]+mergeddf4["PURPOSE"]+mergeddf4["PROMOTE_GOOD"]+mergeddf4["DELAYED_HAPPINESS"]+mergeddf4["CONTENT_RELATIONSHIPS"]+mergeddf4["SATISFYING_RELATIONSHIPS"]+mergeddf4["LIVING_EXPENSES"]+mergeddf4["FOOD_HOUSING"]

frames = [mergeddf2, mergeddf4]
justdf=pd.concat(frames)
justdf=justdf[['DAILY_BREAKS','flourishing_score']]
pv = justdf.corr(method=pearsonr_pval)
print(pv)
