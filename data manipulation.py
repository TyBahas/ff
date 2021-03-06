
# coding: utf-8

# In[338]:


import pandas as pd
import numpy as np
import os


# In[339]:


directory = 'C:/Users/bahasty/Desktop/ff/scores'
pd.set_option('display.max_rows', 500)


# In[340]:


def nameChanger(dataframe):
    dataframe.loc[ dataframe.Team == 'Charlottesville Kaepernicks', 'Team' ] = 'Dan'
    dataframe.loc[ dataframe.Team == '3 Dollar Steak', 'Team' ] = 'Nick'
    dataframe.loc[ dataframe.Team == 'Mahom-osexuals', 'Team' ] = 'Tyler'
    dataframe.loc[ dataframe.Team == 'buckfutt fc (Ryan)', 'Team' ] = 'Ryan'
    dataframe.loc[ dataframe.Team == 'THE ROBERTSONS', 'Team' ] = 'The Robertson'
    dataframe.loc[ dataframe.Team == 'Icebox', 'Team' ] = 'Rebecca'
    dataframe.loc[ dataframe.Team == 'Calrissian Colts', 'Team' ] = 'Brian'
    dataframe.loc[ dataframe.Team == 'buckfutt fc (Alex)', 'Team' ] = 'Alex'
    dataframe.loc[ dataframe.Team == 'The Eastwatch Ice Dragons', 'Team' ] = 'Tony'
    dataframe.loc[ dataframe.Team == 'Scruffy Nerfherders', 'Team' ] = 'Johnny'
    dataframe.loc[ dataframe.Team == 'Optimize', 'Team' ] = 'Dustin'
    dataframe.loc[ dataframe.Team == 'Bronny Football', 'Team' ] = 'Trevor'
    


# In[341]:


#weekly score parser
def WeekParser (xlsx, sheetnum):
    sheet = pd.read_excel(xlsx, 'Sheet'+str(sheetnum))
        
    team1 = sheet.head(22)
    team2 = sheet.tail(23)

    #team 1 formatting
    team1name = team1.columns[0]
    team1 = team1[[team1name,'Unnamed: 6']]
    team1['Team'] = team1name
    team1['Week'] = week
    team1 = team1.drop(team1.index[[0,1,2,12,13,14,15,21]])
    team1.columns = ['Position','Points','Team','Week']
    team1 = team1[['Team','Week','Position','Points']]
    team1 = team1.groupby(['Team','Week','Position']).sum()

    #team 2 formatting
    team2name = team2[team1name].values[0]        
    team2 = team2[[team1name,'Unnamed: 6']]
    team2['Team'] = team2name
    team2['Week'] = week
    team2 = team2.reset_index()
    team2 = team2.drop(team2.index[[0,1,2,3,13,14,15,16,22]])    
    team2.columns = ['index','Position','Points','Team','Week']
    team2 = team2[['Team','Week','Position','Points']]
    team2 = team2.groupby(['Team','Week','Position']).sum()
    
    frames = [team1,team2]
    final = pd.concat(frames)
    return final
    
        


# In[342]:


#creates empty dataframe
columns = ['Team','Week','Position','Points']
dataframe = pd.DataFrame(columns=columns)
weekCount = 0
#iterate over files in scores directory
x = 1
for filename in os.listdir(directory):
    xlsx = pd.ExcelFile(directory+'/'+filename)
    week = os.path.basename(filename)
    week = week[:-5]    
    sheetnum = 1
    
    
    while sheetnum < 7:
        final = WeekParser(xlsx,sheetnum)
        
        if x == 1:
            dataframe = final            
            x = x+1
        else:
            frames = [dataframe,final]
            dataframe = pd.concat(frames)
        
        sheetnum = sheetnum+1
    weekCount = weekCount+1
        


# In[344]:



############################################
#total output ready for Google Chart Paste
############################################

df_sum = dataframe.groupby(['Team','Position']).sum()
df_sum = df_sum.round(2)
df_sum = df_sum.reset_index()
df_sum.columns = ['Team','Position','Total']
df_sum = df_sum.pivot(index='Team', columns='Position', values='Total')
df_sum = df_sum.reset_index()
nameChanger(df_sum)
df_sum['String'] = '[\'' + df_sum['Team'].map(str) +'\',' + df_sum['BN'].map(str) +','+ df_sum['DEF'].map(str)+','+ df_sum['K'].map(str)+','+ df_sum['QB'].map(str)+','+ df_sum['R/W/T'].map(str)  +','+ df_sum['RB'].map(str)  +','+ df_sum['TE'].map(str)  +','+ df_sum['WR'].map(str)+'],'     
df_sum.to_csv('sum.csv', index=False)


# In[345]:



############################################
#position averages overall
############################################

df_avg = dataframe.groupby(['Team','Position']).mean()
df_avg = df_avg.round(2)
df_avg = df_avg.reset_index()
df_avg.columns = ['Team','Position','Average']
df_avg = df_avg.pivot(index='Team', columns='Position', values='Average')
df_avg = df_avg.reset_index()
nameChanger(df_avg)
df_avg['String'] = '[\'' + df_avg['Team'].map(str) +'\',' + df_avg['BN'].map(str) +','+ df_avg['DEF'].map(str)+','+ df_avg['K'].map(str)+','+ df_avg['QB'].map(str)+','+ df_avg['R/W/T'].map(str)  +','+ df_avg['RB'].map(str)  +','+ df_avg['TE'].map(str)  +','+ df_avg['WR'].map(str)+'],'     
df_avg.to_csv('average.csv', index=False)


# In[346]:



############################################
#League data for scatter plot
############################################
#formatting data
league = pd.read_csv('C:/Users/bahasty/Desktop/ff/league/league.csv')
league = league.drop(league.index[[0,1,5,9,13]])   
league['divRank'] = league.Rank.str.slice(0,1)
league['overallRank'] = league.Rank.str.split(pat='[(|)]', expand=True)[1]
league = league[['Team','Stk','For','Against','divRank','overallRank']]
nameChanger(league)


#scatter output
scatter =league[['Team','For','Against']]
scatter = scatter.pivot(index='For', columns='Team', values='Against')
scatter = scatter.reset_index()
scatter['String'] = '[' + scatter['For'].map(str)+','+ scatter['Alex'].map(str) +','+ scatter['Brian'].map(str) +','+ scatter['Dan'].map(str)+','+ scatter['Dustin'].map(str)+','+ scatter['Johnny'].map(str)+','+ scatter['Nick'].map(str)+','+ scatter['Rebecca'].map(str)+','+ scatter['Ryan'].map(str)+','+ scatter['The Robertson'].map(str)+','+ scatter['Tony'].map(str)+','+ scatter['Trevor'].map(str)+','+ scatter['Tyler'].map(str)+'],'    
scatter['String'] = scatter['String'].str.replace('nan','NaN')
scatter.to_csv('scatter.csv', index=False)


# In[350]:


############################################
#Power Ranking
############################################


#creates empty dataframe to collect the last 3 weeks of scores
columns = ['Team','Week','Position','Points']
powerRankingTemp = pd.DataFrame(columns=columns)

powerRanking = dataframe.reset_index()
powerRanking = powerRanking.loc[powerRanking['Position'] != 'BN']
nameChanger(powerRanking)



#creates an array of Week variables that will be used to pull data
weekCountArray = []
x=0
while x <= 2:
    
    if x == 0:
        weekCountArray.append('Week'+ str(weekCount))        
    else:
        weekCountArray.append('Week'+ str(weekCount-x))
    x+=1


#collects the last three weeks found in the weekCountArray and appends them to powerRankingTemp
y = 0
for i in weekCountArray:
    temp = powerRanking.loc[powerRanking['Week'] == weekCountArray[y]]                  
    frames = [powerRankingTemp,temp]
    powerRankingTemp = pd.concat(frames)
    y+=1

    
#Z-Scores based on last 3 Weeks scores
powerRankingLast3Weeks = powerRankingTemp
powerRankingLast3Weeks = powerRankingLast3Weeks.groupby(['Team','Week']).sum()
powerRankingLast3Weeks = powerRankingLast3Weeks.reset_index()
powerRankingLast3Weeks = powerRankingLast3Weeks.groupby(['Team']).mean()
powerRankingLast3Weeks = powerRankingLast3Weeks.reset_index()
teamMean = powerRankingLast3Weeks['Points'].mean()
teamSTD = powerRankingLast3Weeks['Points'].std()
powerRankingLast3Weeks['STD'] = teamSTD
powerRankingLast3Weeks['Mean'] = teamMean
powerRankingLast3Weeks['Z-score'] = (powerRankingLast3Weeks['Points'] - powerRankingLast3Weeks['Mean'] )/ powerRankingLast3Weeks['STD']
powerRankingLast3Weeks.columns = ['Team','Average Weekly Points','Standard Dev','League Mean','Z-Score Ranking']
  
    
#Z-Scores based on median scores
powerRankingMedian = powerRanking.groupby(['Team','Week']).sum()
powerRankingMedian = powerRankingMedian.reset_index()
powerRankingMedian = powerRankingMedian.groupby(['Team']).median()
powerRankingMedian = powerRankingMedian.reset_index()
teamMean = powerRankingMedian['Points'].mean()
teamSTD = powerRankingMedian['Points'].std()
powerRankingMedian['STD'] = teamSTD
powerRankingMedian['Mean'] = teamMean
powerRankingMedian['Z-score'] = (powerRankingMedian['Points'] - powerRankingMedian['Mean'] )/ powerRankingMedian['STD']
powerRankingMedian    

#join power ranking
powerRankingFinal = pd.merge(powerRankingMedian,powerRankingLast3Weeks, left_on='Team', right_on='Team', how='inner')

#formatting
powerRankingFinal = powerRankingFinal[['Team','Z-score','Z-Score Ranking']]
powerRankingFinal['Combined Scores'] = powerRankingFinal[['Z-score','Z-Score Ranking']].mean(axis=1)
powerRankingFinal['Rank'] = powerRankingFinal['Combined Scores'].rank(ascending=False)
powerRankingFinal = powerRankingFinal.sort_values(by=['Rank'])
powerRankingFinal= powerRankingFinal[['Team','Rank']]
powerRankingFinal['String'] = '[\'' + powerRankingFinal['Team'].map(str) +'\',' + powerRankingFinal['Rank'].map(str)+'],'     
powerRankingFinal.to_csv('powerRanking', index=False)

